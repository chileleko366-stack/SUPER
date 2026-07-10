import { z } from "zod";

export const AccentKey = z.enum(["calmInsight", "lightnessEnergy", "tensionBias"]);
export type AccentKey = z.infer<typeof AccentKey>;

export const PrimitiveKind = z.enum([
  "KineticCaption",
  "InfoCard",
  "KenBurnsCard",
  "TimelineReveal",
  "DataChart",
  "CodeBlock",
]);
export type PrimitiveKind = z.infer<typeof PrimitiveKind>;

export const TimelineEventSchema = z.object({
  label: z.string(),
  date: z.string(),
});
export type TimelineEvent = z.infer<typeof TimelineEventSchema>;

export const ChartDatum = z.object({
  label: z.string(),
  value: z.number(),
});
export type ChartDatum = z.infer<typeof ChartDatum>;

export const SegmentSchema = z.object({
  beat: z.string(),
  primitive: PrimitiveKind,
  text: z.string(),
  emphasisWord: z.string().optional(),
  accent: AccentKey,
  voAudioSrc: z.string(),
  durationInFrames: z.number().int().positive(),
  traits: z.array(z.string()).optional(),
  imageSrc: z.string().optional(),
  cutSfx: z.string().optional(),
  // TimelineReveal-only: staggered era/date markers along the horizontal
  // timeline track. See src/remotion/primitives/TimelineReveal.tsx.
  timelineEvents: z.array(TimelineEventSchema).optional(),
  chartData: z.array(ChartDatum).optional(),
  codeLines: z.array(z.string()).optional(),
  language: z.string().optional(),
});
export type Segment = z.infer<typeof SegmentSchema>;

export const TokensSchema = z.object({
  background: z.object({
    explanationBase: z.string(),
    explanationBaseAlt: z.string(),
    infographicCardBg: z.string(),
  }),
  moodAccents: z.object({
    calmInsight: z.object({ primary: z.string(), secondary: z.string() }),
    lightnessEnergy: z.object({ primary: z.string(), secondary: z.string() }),
    tensionBias: z.object({ primary: z.string() }),
  }),
  captionEmphasis: z.string(),
  captionDefault: z.string(),
  fontStack: z.string(),
  // Optional: only required by channels using the TimelineReveal primitive
  // (e.g. Echoes of Ages). Kept optional so existing channels' tokens
  // (e.g. Mind Mosaic, which never renders TimelineReveal) stay valid
  // without change.
  timeline: z
    .object({
      trackColor: z.string(),
      playheadColor: z.string(),
      markerBg: z.string(),
      markerLabel: z.string(),
      eraFill: z.string(),
    })
    .optional(),
  // Optional per-channel signal for motion-intensity-sensitive primitives
  // (currently only DataChart) -- derived from the channel config's
  // motionPersonality.motionIntensity research finding. "energetic" opts
  // into spring/overshoot bar reveals (e.g. Market Lens's measured
  // "pop-in, settle" data-reveal pattern); omitted/"calm" keeps the
  // no-bounce ease-out-cubic default every other primitive uses.
  chartMotion: z.enum(["calm", "energetic"]).optional(),
});
export type Tokens = z.infer<typeof TokensSchema>;

export const ExplainerPropsSchema = z.object({
  channelSlug: z.string(),
  tokens: TokensSchema,
  segments: z.array(SegmentSchema).min(1),
  musicSrc: z.string().optional(),
  musicPolicy: z.string().optional(),
});
export type ExplainerProps = z.infer<typeof ExplainerPropsSchema>;
