import { ProcessInvoiceResponse } from "@/types/invoice";

// const API_BASE_URL = "http://127.0.0.1:8000";
const  API_BASE_URL = process.env.NEXT_PUBLIC_API_URL;

export async function processInvoice(file: File): Promise<ProcessInvoiceResponse> {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(`${API_BASE_URL}/process-invoice`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error("Failed to process invoice.");
  }

  return (await response.json()) as ProcessInvoiceResponse;
}

export async function fetchInvoices() {
  const response = await fetch(`${API_BASE_URL}/invoices`, {
    method: "GET",
    cache: "no-store",
  });

  if (!response.ok) {
    throw new Error("Failed to fetch invoices.");
  }

  return response.json();
}