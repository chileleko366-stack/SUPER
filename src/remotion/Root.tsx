import React from "react";
import { Composition } from "remotion";
import { ExplainerComposition } from "./ExplainerComposition";
import { ExplainerPropsSchema, type ExplainerProps } from "./types";

const FPS = 60;
const WIDTH = 1080;
const HEIGHT = 1920;

const defaultProps: ExplainerProps = {
  channelSlug: "mind-mosaic",
  tokens: {
    background: {
      explanationBase: "#0C0B0B",
      explanationBaseAlt: "#141414",
      infographicCardBg: "#0B1132",
    },
    moodAccents: {
      calmInsight: { primary: "#84BD60", secondary: "#EDF3F2" },
      lightnessEnergy: { primary: "#F0A98B", secondary: "#DACF8D" },
      tensionBias: { primary: "#E2726C" },
    },
    captionEmphasis: "#EFD300",
    captionDefault: "#FFFFFF",
    fontStack: "'Archivo Black', 'Poppins', 'Montserrat', system-ui, sans-serif",
  },
  segments: [
    {
      beat: "hook",
      primitive: "KineticCaption",
      text: "Why do smart people still fall for this",
      emphasisWord: "smart",
      accent: "calmInsight",
      voAudioSrc: "",
      durationInFrames: 180,
    },
  ],
};

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="Explainer"
      component={ExplainerComposition}
      durationInFrames={300}
      fps={FPS}
      width={WIDTH}
      height={HEIGHT}
      defaultProps={defaultProps}
      schema={ExplainerPropsSchema}
      calculateMetadata={async ({ props }) => {
        const total = props.segments.reduce(
          (sum: number, s: { durationInFrames: number }) => sum + s.durationInFrames,
          0
        );
        return { durationInFrames: Math.max(total, 1) };
      }}
    />
  );
};
