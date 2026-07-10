import React from "react";
import { useCurrentFrame, useVideoConfig, interpolate, Easing } from "remotion";
import type { Tokens, AccentKey, TimelineEvent } from "../types";

/**
 * TimelineReveal -- Echoes of Ages' primitive for the "animated camera over
 * history" beat.
 *
 * Design rationale (see research/visual-reference/echoes-of-ages.md): the
 * reference clip (Epic History TV, "Rise of the Ottoman Empire") shows a
 * continuous single-shot animated MAP camera -- a static map asset with a
 * slow pan/zoom, territory-fill color animating in as the narrative
 * advances, and small date-badge markers appearing over time (1289 -> 1300
 * -> 1330 -> 1450 -> 1453). Reproducing that literally would require a real
 * geographic data source (map tiles or a GeoJSON/SVG outline of the actual
 * historical region) that this project does not have and this task does not
 * source -- faking a blob-shaped "map" and calling it geography would be a
 * fabricated component. Instead this primitive honestly builds the part of
 * the reference that IS achievable without geographic data: a horizontal
 * timeline track with staggered era/date markers, a moving "playhead" that
 * stands in for the reference's continuous camera motion, and a territory-
 * style fill bar that sweeps in behind the playhead as an abstract analog
 * for the map's expanding territory-fill (explicitly NOT a map -- no
 * geographic shape is drawn). A real animated map is a legitimate follow-up
 * but needs sourced map data; see VERIFICATION.md "Open Gaps" for this run.
 *
 * Color tokens are the moodboard's own measured hex values (tokens.timeline,
 * populated from channels/echoes-of-ages.json): year-badge navy
 * (#0C1A25), cream map-ink lettering (#D0BBA3), brand red playhead
 * (#D13832), and olive territory-fill (#8B8B70). Fallback defaults below
 * only apply if a channel omits tokens.timeline entirely (so the component
 * never crashes), but Echoes of Ages always supplies the real values.
 */
export const TimelineReveal: React.FC<{
  text: string;
  emphasisWord?: string;
  timelineEvents: TimelineEvent[];
  accent: AccentKey;
  tokens: Tokens;
  durationInFrames: number;
}> = ({ text, emphasisWord, timelineEvents, accent, tokens, durationInFrames }) => {
  const frame = useCurrentFrame();
  const { width, height } = useVideoConfig();

  const timeline = tokens.timeline ?? {
    trackColor: "#0C1A25",
    playheadColor: "#D13832",
    markerBg: "#0C1A25",
    markerLabel: "#D0BBA3",
    eraFill: "#8B8B70",
  };
  const accentColor =
    accent === "tensionBias" ? tokens.moodAccents.tensionBias.primary : tokens.moodAccents[accent].primary;

  const events = timelineEvents.length > 0 ? timelineEvents : [{ label: "", date: "" }];
  const leftPad = width * 0.12;
  const rightPad = width * 0.12;
  const trackWidth = width - leftPad - rightPad;
  const trackY = height * 0.42;

  // Playhead sweeps left -> right across the full beat duration, standing in
  // for the reference's continuous camera pan (smooth ease-in-out, no
  // bounce/overshoot -- moodboard Motion/Pacing: "reads as smooth ease-in-out
  // or linear").
  const playheadProgress = interpolate(frame, [0, durationInFrames], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.inOut(Easing.ease),
  });
  const playheadX = leftPad + trackWidth * playheadProgress;

  // Marker reveal: staggered, one era at a time (InfoCard's proven stagger
  // pattern), independent of playhead position -- documented approximation,
  // not audio-timestamp-synced.
  const staggerStart = 16;
  const staggerGap = Math.max(12, (durationInFrames - staggerStart - 30) / events.length);

  const headlineProgress = interpolate(frame, [0, 10], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });

  const words = text.trim().split(/\s+/);
  const emphasisLower = emphasisWord?.toLowerCase();

  return (
    <div
      style={{
        position: "absolute",
        inset: 0,
        backgroundColor: tokens.background.explanationBaseAlt,
        overflow: "hidden",
      }}
    >
      {/* Territory-fill sweep: an abstract analog of the reference's
          expanding map territory color, NOT a geographic shape. */}
      <div
        style={{
          position: "absolute",
          left: leftPad,
          top: trackY - 3,
          width: Math.max(0, playheadX - leftPad),
          height: 6,
          borderRadius: 3,
          backgroundColor: timeline.eraFill,
          opacity: 0.55,
        }}
      />

      {/* Track */}
      <div
        style={{
          position: "absolute",
          left: leftPad,
          top: trackY,
          width: trackWidth,
          height: 3,
          backgroundColor: timeline.trackColor,
          opacity: 0.85,
        }}
      />

      {/* Playhead */}
      <div
        style={{
          position: "absolute",
          left: playheadX - 2,
          top: trackY - 22,
          width: 4,
          height: 46,
          borderRadius: 2,
          backgroundColor: timeline.playheadColor,
          boxShadow: `0 0 14px ${timeline.playheadColor}`,
        }}
      />

      {/* Era/date markers */}
      {events.map((event, i) => {
        const x =
          events.length > 1
            ? leftPad + (trackWidth * i) / (events.length - 1)
            : leftPad + trackWidth / 2;
        const start = staggerStart + i * staggerGap;
        const p = interpolate(frame, [start, start + 16], [0, 1], {
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
          easing: Easing.out(Easing.back(1.4)),
        });
        const above = i % 2 === 0;

        return (
          <div
            key={i}
            style={{
              position: "absolute",
              left: x,
              top: trackY,
              transform: "translateX(-50%)",
              opacity: p,
            }}
          >
            {/* tick */}
            <div
              style={{
                position: "absolute",
                left: -1,
                top: above ? -18 : 3,
                width: 2,
                height: 18,
                backgroundColor: timeline.trackColor,
              }}
            />
            <div
              style={{
                position: "absolute",
                left: "50%",
                top: above ? -18 - 58 * p : 18 + 40 * (1 - p) + 3,
                transform: `translate(-50%, ${above ? 0 : 0}px) scale(${0.85 + 0.15 * p})`,
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                gap: 6,
                whiteSpace: "nowrap",
              }}
            >
              <div
                style={{
                  backgroundColor: timeline.markerBg,
                  color: timeline.markerLabel,
                  fontFamily: tokens.fontStack,
                  fontWeight: 700,
                  fontSize: 26,
                  padding: "6px 16px",
                  borderRadius: 999,
                  border: `1px solid ${timeline.eraFill}`,
                }}
              >
                {event.date}
              </div>
              <div
                style={{
                  fontFamily: "Georgia, 'Times New Roman', serif",
                  fontWeight: 600,
                  fontStyle: "italic",
                  fontSize: 22,
                  color: timeline.markerLabel,
                  opacity: 0.85,
                  letterSpacing: 0.5,
                  textAlign: "center",
                  maxWidth: 220,
                }}
              >
                {event.label}
              </div>
            </div>
          </div>
        );
      })}

      {/* Caption card: narration line for this beat, snap-in per the
          moodboard's "hard-cut, no fade, one keyword color-punched" caption
          convention (kept as a single card, not per-word, since this beat's
          energy lives in the timeline markers rather than word-by-word
          caption churn). */}
      <div
        style={{
          position: "absolute",
          top: height * 0.69,
          left: 0,
          right: 0,
          padding: "0 64px",
          textAlign: "center",
          opacity: headlineProgress,
          transform: `translateY(${(1 - headlineProgress) * 16}px)`,
        }}
      >
        <span
          style={{
            fontFamily: tokens.fontStack,
            fontWeight: 900,
            textTransform: "uppercase",
            fontSize: 52,
            lineHeight: 1.15,
            textShadow: "0 3px 10px rgba(0,0,0,0.6), 0 0 2px rgba(0,0,0,0.9)",
            WebkitTextStroke: "2px rgba(20,20,20,0.85)",
          }}
        >
          {words.map((word, i) => {
            const cleanWord = word.replace(/[.,!?]/g, "").toLowerCase();
            const isEmphasis = !!emphasisLower && cleanWord === emphasisLower;
            return (
              <span
                key={i}
                style={{
                  color: isEmphasis ? tokens.captionEmphasis : tokens.captionDefault,
                }}
              >
                {word}{" "}
              </span>
            );
          })}
        </span>
      </div>

      {/* Small accent bar, echoing the brand-red logo lockup's fixed
          top-safe-zone presence without claiming to be an actual logo. */}
      <div
        style={{
          position: "absolute",
          top: height * 0.05,
          left: width * 0.08,
          width: 46,
          height: 10,
          borderRadius: 2,
          backgroundColor: accentColor,
        }}
      />
    </div>
  );
};
