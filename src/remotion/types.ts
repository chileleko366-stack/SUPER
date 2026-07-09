import { z } from "zod";

export const AccentKey = z.enum(["calmInsight", "lightnessEnergy", "tensionBias"]);
export type AccentKey = z.infer<typeof AccentKey>;

export const PrimitiveKind = z.enum([
  "KineticCaption",
  "InfoCard",
  "KenBurnsCard",
]);
export type PrimitiveKind = z.infer<typeof PrimitiveKind>;

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
