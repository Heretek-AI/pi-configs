export interface SpecialistMetadata {
  number: string;
  slug: string;
  name: string;
  guild: string;
  model: string;
  thinking: string;
  scope: string;
  owns: string;
  refuses: string;
}

export interface PiToolContext {
  ui: {
    notify(msg: string): void;
    writeBox(text: string): void;
    error(msg: string): void;
  };
  session: {
    setSystemPrompt?(prompt: string): void;
  };
  logger: {
    debug(msg: string): void;
    info(msg: string): void;
    warn(msg: string): void;
    error(msg: string): void;
  };
}

export interface PiRuntime {
  registerCommand(
    name: string,
    options: {
      description?: string;
      handler: (args: string, ctx: PiToolContext) => Promise<void> | void;
    }
  ): void;
  registerTool(tool: {
    name: string;
    description: string;
    parameters: Record<string, unknown>;
    handler?: (params: any, ctx: PiToolContext) => Promise<any> | any;
    execute?: (params: any, ctx: PiToolContext) => Promise<any> | any;
  }): void;
  on(event: string, handler: (ctx: PiToolContext) => Promise<void> | void): void;
}
