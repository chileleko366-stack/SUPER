import React from "react";
import { Img, useCurrentFrame, interpolate, staticFile } from "remotion";
import type { Tokens, AccentKey } from "../types";

/**
 * Slow pan/zoom still, standing in for the moodboard's "single-subject,
 * uncluttered b-roll" beats (research/visual-reference/mind-mosaic.md,
 * Spacing Tokens: "density drops to near-zero during pure b-roll beats").
 * imageSrc is a procedurally generated placeholder card from the pipeline
 * (see pipeline/assets.py) -- real stock-photo sourcing is an open gap,
 * not claimed as solved here.
 */
export const KenBurnsCard: React.FC<{
  imageSrc: string;
  caption?: string;
  accent: AccentKey;
  tokens: Tokens;
  durationInFrames: number;
}> = ({ imageSrc, caption, accent, tokens, durationInFrames }) => {
  const frame = useCurrentFrame();
  const accentColor =
    accent === "tensionBias"
      ? tokens.moodAccents.tensionBias.primary
      : tokens.moodAccents[accent].primary;

  const scale = interpolate(frame, [0, durationInFrames], [1.0, 1.09], {
    extrapolateRight: "clamp",
  });
  const translateX = interpolate(frame, [0, durationInFrames], [0, -18], {
    extrapolateRight: "clamp",
  });

  return (
    <div style={{ position: "absolute", inset: 0, overflow: "hidden", backgroundColor: tokens.background.explanationBase }}>
      <Img
        src={staticFile(imageSrc)}
        style={{
          position: "absolute",
          inset: 0,
          width: "100%",
          height: "100%",
          objectFit: "cover",
          transform: `scale(${scale}) translateX(${translateX}px)`,
        }}
      />
      <div
        style={{
          position: "absolute",
          inset: 0,
          background: "linear-gradient(to top, rgba(0,0,0,0.65), rgba(0,0,0,0) 45%)",
        }}
      />
      {caption ? (
        <div
          style={{
            position: "absolute",
            bottom: 140,
            left: 60,
            right: 60,
            fontFamily: tokens.fontStack,
            fontWeight: 800,
            fontSize: 42,
            color: accentColor,
            textShadow: "0 4px 18px rgba(0,0,0,0.7)",
          }}
        >
          {caption}
        </div>
      ) : null}
    </div>
  );
};
