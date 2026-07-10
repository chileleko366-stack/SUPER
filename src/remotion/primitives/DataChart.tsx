import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate, spring, Easing } from "remotion";
import type { Tokens, AccentKey, ChartDatum } from "../types";

/**
 * Animated vertical bar chart, built from plain SVG + Remotion's own
 * interpolate()/spring() -- no charting library dependency, matching how
 * every other primitive here is built (see InfoCard's staggered reveal,
 * which this follows: one bar at a time, synced to speech, not
 * all-at-once). Numbers are rendered exactly as provided in `data` --
 * this component makes no claim about whether they are real sourced
 * figures or illustrative teaching numbers; that distinction is the
 * pipeline's responsibility (see pipeline/run_channel.py's DataChart
 * handling and each channel's VERIFICATION.md).
 *
 * Motion intensity is channel-controlled via `tokens.chartMotion`:
 * - "calm" (default): ease-out-cubic growth only, no overshoot -- matches
 *   channels whose moodboard found low motion intensity / no bounce
 *   (e.g. Penny Blueprint's measured hard-cut, zero-spring reference clip).
 * - "energetic": spring-based growth with a slight overshoot-and-settle --
 *   matches channels whose moodboard specifically found spring/overshoot
 *   data-reveal motion (e.g. Market Lens's measured "pop in, settle"
 *   checkmark/stat-callout behavior).
 */
export const DataChart: React.FC<{
  headline: string;
  data: ChartDatum[];
  accent: AccentKey;
  tokens: Tokens;
  durationInFrames: number;
}> = ({ headline, data, accent, tokens, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const accentColor =
    accent === "tensionBias"
      ? tokens.moodAccents.tensionBias.primary
      : tokens.moodAccents[accent].primary;
  const energetic = tokens.chartMotion === "energetic";

  const headlineProgress = interpolate(frame, [0, 18], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });

  const staggerStart = 24;
  const staggerGap = Math.max(
    10,
    (durationInFrames - staggerStart - 24) / Math.max(data.length, 1)
  );

  const chartWidth = 860;
  const chartHeight = 520;
  const barGap = 26;
  const barCount = Math.max(data.length, 1);
  const barWidth = (chartWidth - barGap * (barCount - 1)) / barCount;
  const maxValue = Math.max(...data.map((d) => Math.abs(d.value)), 1);

  const formatValue = (v: number): string => {
    const rounded = Math.round(v * 100) / 100;
    if (Number.isInteger(rounded)) return rounded.toLocaleString("en-US");
    return rounded.toLocaleString("en-US", { maximumFractionDigits: 2 });
  };

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
        gap: 36,
      }}
    >
      <div
        style={{
          fontFamily: tokens.fontStack,
          fontWeight: 900,
          textTransform: "uppercase",
          fontSize: 48,
          textAlign: "center",
          color: tokens.captionDefault,
          opacity: headlineProgress,
          transform: `translateY(${(1 - headlineProgress) * 20}px)`,
          padding: "0 60px",
        }}
      >
        {headline}
      </div>

      <svg
        width={chartWidth}
        height={chartHeight + 90}
        viewBox={`0 0 ${chartWidth} ${chartHeight + 90}`}
        style={{ overflow: "visible" }}
      >
        <line
          x1={0}
          y1={chartHeight}
          x2={chartWidth}
          y2={chartHeight}
          stroke={tokens.captionDefault}
          strokeOpacity={0.25}
          strokeWidth={2}
        />

        {data.map((d, i) => {
          const start = staggerStart + i * staggerGap;
          const localFrame = frame - start;

          let p: number;
          if (energetic) {
            p = spring({
              frame: localFrame,
              fps,
              config: { damping: 12, stiffness: 140, mass: 0.6 },
              durationInFrames: 26,
            });
          } else {
            p = interpolate(localFrame, [0, 18], [0, 1], {
              extrapolateLeft: "clamp",
              extrapolateRight: "clamp",
              easing: Easing.out(Easing.cubic),
            });
          }
          p = Math.max(0, p);

          const heightFrac = Math.abs(d.value) / maxValue;
          const barHeight = Math.max(0, heightFrac * chartHeight * Math.min(p, 1.15));
          const x = i * (barWidth + barGap);
          const y = chartHeight - barHeight;

          const labelOpacity = interpolate(localFrame, [0, 12], [0, 1], {
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
          });

          return (
            <g key={i}>
              <rect
                x={x}
                y={y}
                width={barWidth}
                height={barHeight}
                fill={accentColor}
                rx={10}
              />
              <text
                x={x + barWidth / 2}
                y={Math.max(y - 16, 28)}
                textAnchor="middle"
                fill={tokens.captionDefault}
                fontFamily={tokens.fontStack}
                fontWeight={800}
                fontSize={34}
                opacity={labelOpacity}
              >
                {formatValue(d.value)}
              </text>
              <text
                x={x + barWidth / 2}
                y={chartHeight + 44}
                textAnchor="middle"
                fill={tokens.captionDefault}
                fontFamily={tokens.fontStack}
                fontWeight={600}
                fontSize={26}
                opacity={labelOpacity}
              >
                {d.label}
              </text>
            </g>
          );
        })}
      </svg>
    </div>
  );
};
