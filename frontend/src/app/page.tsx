"use client";

import { useState } from "react";

import { InvoiceUploader } from "@/components/invoice-uploader";
import { ResultsPanel } from "@/components/results-panel";
import InvoiceHistory from "@/components/invoice-history";
import { ProcessInvoiceResponse } from "@/types/invoice";

export default function Home() {
  const [result, setResult] = useState<ProcessInvoiceResponse | null>(null);

  return (
    <main className="min-h-screen bg-black text-white p-6">
      
      <h1 className="text-3xl font-bold mb-6 text-center">
        Invoice AI System
      </h1>

      <div className="grid gap-6 md:grid-cols-2">
        
        {/* LEFT SIDE */}
        <div className="space-y-6">
          <InvoiceUploader onSuccess={setResult} />
          <InvoiceHistory />
        </div>

        {/* RIGHT SIDE */}
        <ResultsPanel result={result} />

      </div>
    </main>
  );
}
