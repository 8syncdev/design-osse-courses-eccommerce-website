import CountDownDEV from "@/components/comp_dev/CountDownDEV/CountDownDEV"
import Section from "@/components/comp_dev/Section/Section"
import { Button } from "@/components/ui/button"
import Link from "next/link"



export default function CourseLayout({
    children,
}: {
    children: React.ReactNode
}) {
    return (
        <>
            <Section>
                <div className='h-full grid grid-cols-12 w-full relative z-10'>
                    <div className="md:col-span-8 col-span-12 md:mb-0 mb-10">
                        <p className='text-xl border-l-2 border-b-2 border-[#0ff] w-fit px-5 py-2 rounded-xl mb-5'>Khóa Học</p>
                        {children}
                    </div>
                    <div className="md:col-span-4 col-span-12 md:pl-5 pl-0">
                        <p className='text-xl border-l-2 border-b-2 border-[#0ff] w-fit px-5 py-2 rounded-xl mb-5'>Thông Báo</p>
                        <div className="pl-3 border-l-2 mb-5">
                            <p className="mb-3">Thời gian đăng kí tài khoản
                                <span className="text-neon">PREMIUM</span> đang được giảm giá và dùng trọn đời !!!
                            </p>
                            <p className="mb-2">Giá Gốc: <span className="line-through">2.500.000</span></p>
                            <p>Giá Hiện Tại: <span className="shadow-sm-neon p-1 rounded-sm">500.000</span></p>
                            <div className="pt-10 flex flex-col gap-3 items-center">
                                <Button className="">
                                    <Link href="#" target="_blank">Liên Hệ Admin</Link>
                                </Button>
                                <Button>
                                    <Link href="#" target="_blank">Liên Hệ Tư Vấn</Link>
                                </Button>
                            </div>
                        </div>
                        <div className="md:px-0 sm:px-20 px-5">
                            <CountDownDEV showText={true} />
                        </div>
                    </div>
                </div>
            </Section>
        </>
    )
}