import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate, Easing } from "remotion";
import type { Tokens, AccentKey } from "../types";
import { AmbientOrb } from "./AmbientOrb";

/**
 * Word-by-word kinetic caption. Two-tier emphasis (default white, one gold
 * keyword) and per-word ease-out entrance -- no bounce/overshoot, per the
 * Mind Mosaic moodboard's motion-intensity finding (research/visual-reference/mind-mosaic.md).
 * Positioned in the observed "caption safe zone" (~60-78% of frame height).
 * AmbientOrb is rendered as a sibling (not nested in the caption box) so it
 * sits low in the full frame rather than overlapping caption text.
 */
export const KineticCaption: React.FC<{
  text: string;
  emphasisWord?: string;
  accent: AccentKey;
  tokens: Tokens;
  durationInFrames: number;
}> = ({ text, emphasisWord, accent, tokens, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { height } = useVideoConfig();
  const words = text.trim().split(/\s+/);

  // The emphasized keyword always uses the gold captionEmphasis token
  // observed directly in the reference clip
  // (research/visual-reference/mind-mosaic.md) -- independent of the
  // per-beat mood accent, which is a separate finding (see InfoCard/
  // KenBurnsCard, where `accent` does drive scene color).
  void accent;

  const revealSpanFrames = Math.min(durationInFrames * 0.6, words.length * 10);
  const perWord = revealSpanFrames / Math.max(words.length, 1);

  return (
    <>
      <AmbientOrb />
      <div
        style={{
          position: "absolute",
          top: height * 0.6,
          left: 0,
          right: 0,
          height: height * 0.15,
          display: "flex",
          flexWrap: "wrap",
          alignContent: "center",
          justifyContent: "center",
          gap: "0 18px",
          padding: "0 64px",
        }}
      >
        {words.map((word, i) => {
          const startFrame = i * perWord;
          const progress = interpolate(
            frame,
            [startFrame, startFrame + 14],
            [0, 1],
            { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) }
          );
          // Exact match, or simple prefix match to tolerate NIM returning a
          // word-form variant (e.g. "decisions" vs. the script's "decision").
          const cleanWord = word.replace(/[.,!?]/g, "").toLowerCase();
          const emphasisLower = emphasisWord?.toLowerCase();
          const isEmphasis =
            !!emphasisLower &&
            (cleanWord === emphasisLower ||
              (cleanWord.length > 3 &&
                emphasisLower.length > 3 &&
                (cleanWord.startsWith(emphasisLower.slice(0, -1)) ||
                  emphasisLower.startsWith(cleanWord.slice(0, -1)))));

          return (
            <span
              key={i}
              style={{
                fontFamily: tokens.fontStack,
                fontWeight: 900,
                textTransform: "uppercase",
                fontSize: 64,
                lineHeight: 1.05,
                color: isEmphasis ? tokens.captionEmphasis : tokens.captionDefault,
                opacity: progress,
                transform: `translateY(${(1 - progress) * 24}px)`,
                textShadow: "0 4px 18px rgba(0,0,0,0.55)",
              }}
            >
              {word}
            </span>
          );
        })}
      </div>
    </>
  );
};
