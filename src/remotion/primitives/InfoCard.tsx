import React from "react";
import { useCurrentFrame, interpolate, Easing } from "remotion";
import type { Tokens, AccentKey } from "../types";

/**
 * Full-bleed concept/mechanism card with a staggered, one-at-a-time reveal
 * of trait/keyword items -- matches the moodboard's observed "incremental
 * reveal synced to speech" pattern (research/visual-reference/mind-mosaic.md,
 * Spacing Tokens), not an all-at-once list.
 */
export const InfoCard: React.FC<{
  headline: string;
  traits: string[];
  accent: AccentKey;
  tokens: Tokens;
  durationInFrames: number;
}> = ({ headline, traits, accent, tokens, durationInFrames }) => {
  const frame = useCurrentFrame();
  const accentColor =
    accent === "tensionBias"
      ? tokens.moodAccents.tensionBias.primary
      : tokens.moodAccents[accent].primary;

  const headlineProgress = interpolate(frame, [0, 18], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });

  const staggerStart = 22;
  const staggerGap = Math.max(
    14,
    (durationInFrames - staggerStart - 20) / Math.max(traits.length, 1)
  );

  return (
    <div
      style={{
        position: "absolute",
        inset: 0,
        backgroundColor: tokens.background.infographicCardBg,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        gap: 40,
      }}
    >
      <div
        style={{
          fontFamily: tokens.fontStack,
          fontWeight: 900,
          textTransform: "uppercase",
          fontSize: 56,
          textAlign: "center",
          color: accentColor,
          opacity: headlineProgress,
          transform: `translateY(${(1 - headlineProgress) * 20}px)`,
          padding: "0 60px",
        }}
      >
        {headline}
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: 22 }}>
        {traits.map((trait, i) => {
          const start = staggerStart + i * staggerGap;
          const p = interpolate(frame, [start, start + 16], [0, 1], {
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
            easing: Easing.out(Easing.cubic),
          });
          return (
            <div
              key={i}
              style={{
                display: "flex",
                alignItems: "center",
                gap: 18,
                opacity: p,
                transform: `translateX(${(1 - p) * -24}px)`,
              }}
            >
              <div
                style={{
                  width: 20,
                  height: 20,
                  borderRadius: "50%",
                  backgroundColor: accentColor,
                  flexShrink: 0,
                }}
              />
              <span
                style={{
                  fontFamily: tokens.fontStack,
                  fontWeight: 700,
                  fontSize: 40,
                  color: tokens.captionDefault,
                }}
              >
                {trait}
              </span>
            </div>
          );
        })}
      </div>
    </div>
  );
};
