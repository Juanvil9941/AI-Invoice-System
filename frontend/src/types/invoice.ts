export interface AgentResult {
  agent: string;
  status: string;
  reason: string;
}

export interface FinalDecision {
  decision: string;
  issues: AgentResult[];
}

export interface SimilarInvoice {
  score: number;
  payload: {
    text_preview?: string;
    decision?: string;
  };
}

export interface ProcessInvoiceResponse {
  text_preview: string;
  agent_results: AgentResult[];
  final_decision: FinalDecision;
  similar_invoices: SimilarInvoice[];
}