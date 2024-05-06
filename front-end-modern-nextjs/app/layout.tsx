import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./_style/globals.css";
import "./_style/dev_core.css";
import { imgIconBrand14 } from "@/src/constant/image";
import SecurityProvider from "@/src/provider/SecurityProvider";

// import "./_style/theme.css";

const inter = Inter({ subsets: ["latin"] });
export const metadata: Metadata = {
  title: "8 Sync Dev",
  description: "Thổi bùng sức mạnh của bạn",
  icons: [
    {
      url: imgIconBrand14.src,
      sizes: "any",
      rel: "icon",
    }
  ]
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {


  return (
    <SecurityProvider onSecurity={false}>
      <html lang="vi" className="scroll-smooth">
        {/* <link rel="icon" href="/images/_brand/brand-13.png" sizes="any" /> */}
        <body className={`${inter.className}`}>
          {children}
        </body>
      </html>
    </SecurityProvider>
  );
}



