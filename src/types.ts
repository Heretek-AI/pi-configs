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

export interface ExtensionUIDialogOptions {
  signal?: AbortSignal;
  timeout?: number;
}

export interface ExtensionUIContext {
  notify(message: string, type?: 'info' | 'warning' | 'error'): void;
  select(title: string, options: string[], opts?: ExtensionUIDialogOptions): Promise<string | undefined>;
  confirm(title: string, message: string, opts?: ExtensionUIDialogOptions): Promise<boolean>;
  input(title: string, placeholder?: string, opts?: ExtensionUIDialogOptions): Promise<string | undefined>;
  setStatus(key: string, text: string | undefined): void;
  pasteToEditor?(text: string): void;
}

export interface ExtensionCommandContext {
  ui: ExtensionUIContext;
  hasUI: boolean;
  cwd: string;
  isIdle?(): boolean;
}

export interface BeforeAgentStartEvent {
  type: 'before_agent_start';
  systemPrompt?: string;
  systemPromptOptions?: {
    appendSystemPrompt?: string[];
    [key: string]: unknown;
  };
}

export interface PiRuntime {
  registerCommand(
    name: string,
    options: {
      description?: string;
      handler: (args: string, ctx: ExtensionCommandContext) => Promise<void> | void;
    }
  ): void;
  registerTool(tool: {
    name: string;
    description: string;
    parameters: Record<string, unknown>;
    handler?: (params: any, ctx: ExtensionCommandContext) => Promise<any> | any;
    execute?: (params: any, ctx: ExtensionCommandContext) => Promise<any> | any;
  }): void;
  on(event: string, handler: (event: any, ctx: ExtensionCommandContext) => Promise<any> | any): () => void;
}
