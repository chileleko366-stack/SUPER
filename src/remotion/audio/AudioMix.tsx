import React from "react";
import { Audio, Sequence, interpolate, staticFile } from "remotion";
import type { Segment } from "../types";

const FPS = 60;
const DUCK_BASELINE = 0.16; // music level under continuous VO
const DUCK_AT_CUT = 0.05; // deeper dip right at a hard cut / SFX hit
const FADE_FRAMES = 24; // ~0.4s at 60fps

/**
 * Shared audio-mix module: music bed ducks under VO for the whole runtime,
 * dips further for ~0.3s around every hard-cut boundary (where an SFX hit
 * also fires), and fades in/out at the very start/end. VO clips are placed
 * per-segment; SFX clips fire at each segment boundary. This is a single
 * volume-envelope function evaluated per-frame, not a static mix -- per the
 * Phase 3 spec's explicit "not a static mix" requirement.
 */
function buildCutFrames(segments: Segment[]): number[] {
  const cuts: number[] = [];
  let acc = 0;
  for (const seg of segments) {
    cuts.push(acc);
    acc += seg.durationInFrames;
  }
  return cuts; // includes frame 0 (hook start) and every subsequent hard cut
}

export const AudioMix: React.FC<{
  segments: Segment[];
  musicSrc?: string;
  totalDurationInFrames: number;
}> = ({ segments, musicSrc, totalDurationInFrames }) => {
  const cutFrames = buildCutFrames(segments);

  const musicVolume = (frame: number): number => {
    // Start/end fade.
    const fadeIn = interpolate(frame, [0, FADE_FRAMES], [0, 1], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    });
    const fadeOut = interpolate(
      frame,
      [totalDurationInFrames - FADE_FRAMES, totalDurationInFrames],
      [1, 0],
      { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
    );

    // Duck dip around the nearest cut boundary (dip-and-recover envelope).
    let dip = 1;
    for (const cut of cutFrames) {
      const distance = frame - cut;
      if (distance >= -6 && distance <= 18) {
        const local =
          distance < 0
            ? interpolate(distance, [-6, 0], [1, 0], { extrapolateLeft: "clamp" })
            : interpolate(distance, [0, 18], [0, 1], { extrapolateRight: "clamp" });
        dip = Math.min(dip, local);
      }
    }

    const baseline = interpolate(dip, [0, 1], [DUCK_AT_CUT, DUCK_BASELINE]);
    return baseline * fadeIn * fadeOut;
  };

  let offset = 0;
  const voSequences = segments.map((seg, i) => {
    const el = (
      <Sequence key={`vo-${i}`} from={offset} durationInFrames={seg.durationInFrames}>
        <Audio src={staticFile(seg.voAudioSrc)} volume={1} />
      </Sequence>
    );
    offset += seg.durationInFrames;
    return el;
  });

  const sfxSequences = segments
    .map((seg, i) => ({ seg, cutFrame: cutFrames[i] }))
    .filter(({ seg }) => Boolean(seg.cutSfx))
    .map(({ seg, cutFrame }, i) => (
      <Sequence key={`sfx-${i}`} from={cutFrame} durationInFrames={Math.round(0.5 * FPS)}>
        <Audio src={staticFile(seg.cutSfx as string)} volume={0.55} />
      </Sequence>
    ));

  return (
    <>
      {musicSrc ? (
        <Audio src={staticFile(musicSrc)} volume={musicVolume} loop />
      ) : null}
      {voSequences}
      {sfxSequences}
    </>
  );
};
