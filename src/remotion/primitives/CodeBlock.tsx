import React from "react";
import { useCurrentFrame, interpolate, Easing } from "remotion";
import type { Tokens, AccentKey } from "../types";

/**
 * Code/pseudocode snippet card: line-by-line reveal, monospace body, simple
 * regex-based keyword tinting. No syntax-highlighting library -- deterministic
 * plain React/CSS tokenizer, matching every other primitive in this repo.
 *
 * Design decisions, grounded in research/visual-reference/code-trail.md:
 * - Near-black/charcoal panel (`tokens.background.infographicCardBg`) with a
 *   pure-white 2px header-divider hairline -- the moodboard's "grid divider
 *   rules -- pure white, ~2px hairlines" + "UI chrome stays strictly
 *   black-and-white" finding.
 * - A persistent small header row (title + language label) echoes the
 *   moodboard's "one persistent dashboard-chrome element" motif (its
 *   reference clip used a live iteration counter; here it's a static
 *   file/language label since a code snippet has no natural counter).
 * - The left accent bar hue-cycles slowly and continuously (reusing the
 *   AmbientOrb technique) -- this is the nod to the moodboard's headline
 *   finding, "a near-black dashboard base with a single saturated,
 *   continuously hue-rotating accent." Keyword-tint colors themselves are
 *   deliberately NOT hue-cycled and stay fixed to the accent token: cycling
 *   the actual code-text color would hurt legibility and overshoot the
 *   moodboard's own "moderate" motion-intensity finding, which reserves
 *   punchy/attention motion for chrome, not body content.
 * - Reveal is line-by-line with simple ease-out (no bounce/overshoot), per
 *   "simple eased transitions...rather than bouncy...moves, which would read
 *   as playful/lifestyle rather than technical."
 */

const KEYWORD_RE =
  /\b(function|const|let|var|if|else|for|while|return|def|class|import|from|export|default|new|typeof|in|of|true|false|null|None|True|False|break|continue|switch|case|try|except|catch|finally|async|await|print|self|this|public|private|static|void|int|str|string|struct|impl|fn|pub|match)\b/;
const STRING_RE = /("(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|`(?:[^`\\]|\\.)*`)/;
const COMMENT_RE = /(\/\/.*$|#.*$)/;
const NUMBER_RE = /\b(\d+(?:\.\d+)?)\b/;

// Ordered alternation: comments win over everything past their start,
// then strings, then keywords, then numbers, then plain text runs.
const TOKEN_RE = new RegExp(
  `(${COMMENT_RE.source})|(${STRING_RE.source})|(${KEYWORD_RE.source})|(${NUMBER_RE.source})`,
  "g"
);

type TokenKind = "comment" | "string" | "keyword" | "number" | "plain";

interface CodeToken {
  text: string;
  kind: TokenKind;
}

/** Deterministic line tokenizer -- splits on the ordered regex above and
 * labels the gaps as plain text. No external dependency. */
function tokenizeLine(line: string): CodeToken[] {
  const tokens: CodeToken[] = [];
  let lastIndex = 0;
  TOKEN_RE.lastIndex = 0;
  let match: RegExpExecArray | null;

  while ((match = TOKEN_RE.exec(line)) !== null) {
    if (match.index > lastIndex) {
      tokens.push({ text: line.slice(lastIndex, match.index), kind: "plain" });
    }
    const [full, comment, string, , keyword, , number] = match;
    let kind: TokenKind = "plain";
    if (comment) kind = "comment";
    else if (string) kind = "string";
    else if (keyword) kind = "keyword";
    else if (number) kind = "number";
    tokens.push({ text: full, kind });
    lastIndex = match.index + full.length;

    if (comment) break; // rest of line is inside the comment
  }
  if (lastIndex < line.length) {
    tokens.push({ text: line.slice(lastIndex), kind: "plain" });
  }
  return tokens;
}

function tokenColor(kind: TokenKind, accentColor: string, tokens: Tokens): string {
  switch (kind) {
    case "keyword":
      return accentColor;
    case "string":
      return tokens.captionEmphasis;
    case "comment":
      return "#7A8080";
    case "number":
      return "#D8D2C4";
    default:
      return tokens.captionDefault;
  }
}

export const CodeBlock: React.FC<{
  title: string;
  codeLines: string[];
  language?: string;
  accent: AccentKey;
  tokens: Tokens;
  durationInFrames: number;
}> = ({ title, codeLines, language, accent, tokens, durationInFrames }) => {
  const frame = useCurrentFrame();
  const accentColor =
    accent === "tensionBias"
      ? tokens.moodAccents.tensionBias.primary
      : tokens.moodAccents[accent].primary;

  // Slow continuous hue-cycle for the accent bar only -- see file header
  // comment for why this is scoped to chrome, not code-text color.
  const cycleFrames = 480; // 8s @ 60fps
  const hueT = (frame / cycleFrames) % 1;
  const barHue = interpolate(hueT, [0, 1], [0, 360]);

  const headerProgress = interpolate(frame, [0, 14], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });

  const revealStart = 18;
  const revealEnd = Math.max(revealStart + codeLines.length * 8, durationInFrames * 0.55);
  const perLine = (revealEnd - revealStart) / Math.max(codeLines.length, 1);

  return (
    <div
      style={{
        position: "absolute",
        inset: 0,
        backgroundColor: tokens.background.explanationBase,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        padding: "0 56px",
      }}
    >
      <div
        style={{
          width: "100%",
          maxWidth: 940,
          backgroundColor: tokens.background.infographicCardBg,
          borderRadius: 14,
          overflow: "hidden",
          boxShadow: "0 20px 60px rgba(0,0,0,0.55)",
          opacity: headerProgress,
          transform: `translateY(${(1 - headerProgress) * 16}px)`,
        }}
      >
        {/* Header row: title + language, pure-white 2px hairline divider
            below it, per moodboard grid-divider finding. */}
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            padding: "20px 26px",
            borderBottom: "2px solid #FFFFFF",
          }}
        >
          <span
            style={{
              fontFamily: tokens.fontStack,
              fontWeight: 600,
              fontSize: 26,
              color: tokens.captionDefault,
              overflow: "hidden",
              textOverflow: "ellipsis",
              whiteSpace: "nowrap",
              flexShrink: 1,
              minWidth: 0,
            }}
          >
            {title}
          </span>
          {language ? (
            <span
              style={{
                fontFamily: "'JetBrains Mono', 'Fira Code', 'Consolas', monospace",
                fontWeight: 500,
                fontSize: 20,
                color: "#9AA0A0",
                textTransform: "lowercase",
                flexShrink: 0,
                marginLeft: 16,
              }}
            >
              {language}
            </span>
          ) : null}
        </div>

        {/* Body: accent bar (hue-cycling chrome) + monospace code lines. */}
        <div style={{ display: "flex" }}>
          <div
            style={{
              width: 6,
              flexShrink: 0,
              backgroundColor: `hsl(${barHue}, 78%, 52%)`,
            }}
          />
          <div style={{ padding: "26px 30px", display: "flex", flexDirection: "column", gap: 4 }}>
            {codeLines.map((line, i) => {
              const start = revealStart + i * perLine;
              const p = interpolate(frame, [start, start + 12], [0, 1], {
                extrapolateLeft: "clamp",
                extrapolateRight: "clamp",
                easing: Easing.out(Easing.cubic),
              });
              const lineTokens = tokenizeLine(line);

              return (
                <div
                  key={i}
                  style={{
                    display: "flex",
                    opacity: p,
                    transform: `translateX(${(1 - p) * -14}px)`,
                    fontFamily: "'JetBrains Mono', 'Fira Code', 'Consolas', monospace",
                    fontSize: 27,
                    lineHeight: 1.55,
                    whiteSpace: "pre",
                  }}
                >
                  <span style={{ color: "#5B6161", width: 34, flexShrink: 0, userSelect: "none" }}>
                    {i + 1}
                  </span>
                  <span
                    style={{
                      display: "inline-block",
                      overflow: "hidden",
                      textOverflow: "ellipsis",
                      maxWidth: 800,
                      verticalAlign: "top",
                    }}
                  >
                    {lineTokens.map((tok, j) => (
                      <span key={j} style={{ color: tokenColor(tok.kind, accentColor, tokens) }}>
                        {tok.text}
                      </span>
                    ))}
                  </span>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
};
