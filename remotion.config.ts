import { Config } from "@remotion/cli/config";

// Phase 3 confirmed spec: 60fps, 1080x1920, hard cuts only, bt709 color.
Config.setVideoImageFormat("jpeg");
Config.setJpegQuality(80);
Config.setCodec("h264");
Config.setCrf(19);
Config.setColorSpace("bt709");
Config.setConcurrency(2);
