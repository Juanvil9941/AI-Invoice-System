import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Invoice AI System",
  description: "Upload invoices, review AI analysis, and browse recent invoice decisions.",
};

type RootLayoutProps = {
  children: React.ReactNode;
};

export default function RootLayout({ children }: RootLayoutProps) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-neutral-950 text-neutral-100 antialiased">
        <div className="min-h-screen bg-[radial-gradient(circle_at_top,_rgba(64,64,64,0.2),_transparent_45%),linear-gradient(180deg,_#171717_0%,_#0a0a0a_100%)]">
          {children}
        </div>
      </body>
    </html>
  );
}