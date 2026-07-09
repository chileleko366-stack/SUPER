import React from "react";
import { useCurrentFrame, interpolate } from "remotion";

/**
 * Continuous hue-cycling ambient motion for held shots, standing in for the
 * decorative orb observed in the Mind Mosaic reference clip (moodboard:
 * "ambient motion used to keep static shots visually alive between hard
 * cuts" -- deliberately slow/continuous, never a spring/overshoot, per the
 * moodboard's "avoid bounce/overshoot" motion-intensity finding).
 */
export const AmbientOrb: React.FC<{ size?: number; cycleSeconds?: number }> = ({
  size = 140,
  cycleSeconds = 8,
}) => {
  const frame = useCurrentFrame();
  const fps = 60;
  const t = (frame / (cycleSeconds * fps)) % 1;
  const hue = interpolate(t, [0, 1], [0, 360]);

  return (
    <div
      style={{
        position: "absolute",
        bottom: 90,
        left: "50%",
        transform: "translateX(-50%)",
        width: size,
        height: size,
        borderRadius: "50%",
        background: `radial-gradient(circle at 35% 35%, hsl(${hue}, 85%, 65%), hsl(${(hue + 40) % 360}, 80%, 35%) 70%)`,
        filter: "blur(2px)",
        opacity: 0.55,
      }}
    />
  );
};
