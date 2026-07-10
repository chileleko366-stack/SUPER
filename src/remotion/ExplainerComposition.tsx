import React from "react";
import { AbsoluteFill, Sequence } from "remotion";
import type { ExplainerProps } from "./types";
import { KineticCaption } from "./primitives/KineticCaption";
import { InfoCard } from "./primitives/InfoCard";
import { KenBurnsCard } from "./primitives/KenBurnsCard";
import { TimelineReveal } from "./primitives/TimelineReveal";
import { DataChart } from "./primitives/DataChart";
import { CodeBlock } from "./primitives/CodeBlock";
import { AudioMix } from "./audio/AudioMix";

/**
 * General-purpose explainer/storytelling composition -- built from the Mind
 * Mosaic moodboard tokens but not psychology-specific (per Phase 7 pilot
 * instructions: reused as-is for the generic-tier channels in Step 2).
 * Hard cuts only: each beat is a plain <Sequence> boundary, no crossfade.
 */
export const ExplainerComposition: React.FC<ExplainerProps> = ({
  tokens,
  segments,
  musicSrc,
}) => {
  const totalDurationInFrames = segments.reduce((sum, s) => sum + s.durationInFrames, 0);

  let offset = 0;

  return (
    <AbsoluteFill style={{ backgroundColor: tokens.background.explanationBase }}>
      {segments.map((seg, i) => {
        const from = offset;
        offset += seg.durationInFrames;

        return (
          <Sequence key={i} from={from} durationInFrames={seg.durationInFrames}>
            <AbsoluteFill style={{ backgroundColor: tokens.background.explanationBase }}>
              {seg.primitive === "KineticCaption" && (
                <KineticCaption
                  text={seg.text}
                  emphasisWord={seg.emphasisWord}
                  accent={seg.accent}
                  tokens={tokens}
                  durationInFrames={seg.durationInFrames}
                />
              )}
              {seg.primitive === "InfoCard" && (
                <InfoCard
                  headline={seg.text}
                  traits={seg.traits ?? []}
                  accent={seg.accent}
                  tokens={tokens}
                  durationInFrames={seg.durationInFrames}
                />
              )}
              {seg.primitive === "KenBurnsCard" && seg.imageSrc && (
                <KenBurnsCard
                  imageSrc={seg.imageSrc}
                  caption={seg.text}
                  accent={seg.accent}
                  tokens={tokens}
                  durationInFrames={seg.durationInFrames}
                />
              )}
              {seg.primitive === "TimelineReveal" && seg.timelineEvents && (
                <TimelineReveal
                  text={seg.text}
                  emphasisWord={seg.emphasisWord}
                  timelineEvents={seg.timelineEvents}
                  accent={seg.accent}
                  tokens={tokens}
                  durationInFrames={seg.durationInFrames}
                />
              )}
              {seg.primitive === "DataChart" && seg.chartData && (
                <DataChart
                  headline={seg.text}
                  data={seg.chartData}
                  accent={seg.accent}
                  tokens={tokens}
                  durationInFrames={seg.durationInFrames}
                />
              )}
              {seg.primitive === "CodeBlock" && seg.codeLines && (
                <CodeBlock
                  title={seg.text}
                  codeLines={seg.codeLines}
                  language={seg.language}
                  accent={seg.accent}
                  tokens={tokens}
                  durationInFrames={seg.durationInFrames}
                />
              )}
            </AbsoluteFill>
          </Sequence>
        );
      })}

      <AudioMix
        segments={segments}
        musicSrc={musicSrc}
        totalDurationInFrames={totalDurationInFrames}
      />
    </AbsoluteFill>
  );
};
