import { TransitionProvider } from "@/src/provider";
import Background from "@/components/comp_dev/BackgroundDEV/Background";
import HeaderDEV from "@/components/comp_dev/HeaderDEV/HeaderDEV";
import { Toaster } from "@/components/ui/sonner";
import NavRoute from "@/components/comp_dev/NavRoute/NavRoute";
import { Metadata } from "next";


export default function EndUserLayout({
    children,
}: {
    children: React.ReactNode
}) {
    return (
        <>
            <div className="min-h-screen h-auto w-full overflow-x-hidden overflow-y-auto relative z-5">
                {/* Backgroud wrap all components */}
                <Background />
                {/* Header Component  */}
                <HeaderDEV />
                <TransitionProvider>
                    <NavRoute />
                    {children}
                </TransitionProvider>
            </div>
            <Toaster className="bg-black/75 text-white" />
        </>
    )
}

