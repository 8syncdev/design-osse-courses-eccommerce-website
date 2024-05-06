import React from 'react'
import {
    Sheet,
    SheetContent,
    SheetDescription,
    SheetHeader,
    SheetTitle,
    SheetTrigger,
} from "@/components/ui/sheet"
import Link from 'next/link'
import { AlignJustify } from 'lucide-react'




const MobileNavDEV = ({
    className,

}: {
    className?: string
}) => {
    return (
        <Sheet>
            <SheetTrigger>
                <AlignJustify />
            </SheetTrigger>
            <SheetContent className='bg-bgsecondary border-[#0ff] shadow-sm-neon'>
                <SheetHeader>
                    <SheetTitle className='text-cyan-50 border-b-2 border-[#0ff]'>
                        Bạn có tài khoản PREMIUM chưa?
                    </SheetTitle>
                </SheetHeader>
                <SheetDescription className='text-cyan-100 flex-col flex gap-7 pt-10'>
                    <Link href='/' className='border-b-2 px-3 border-x-2 border-[#0ff] rounded-full hover:shadow-sm-neon transition-slow-1 relative z-10 py-[1rem] text-center text-lg'>
                        Home
                    </Link>
                    <Link href='/course' className='border-b-2 px-3 border-x-2 border-[#0ff] rounded-full hover:shadow-sm-neon transition-slow-1 relative z-10 py-[1rem] text-center text-lg'>
                        Khóa học
                    </Link>
                    <Link href='/' className='border-b-2 px-3 border-x-2 border-[#0ff] rounded-full hover:shadow-sm-neon transition-slow-1 relative z-10 py-[1rem] text-center text-lg'>
                        About
                    </Link>
                    <Link href='/' className='border-b-2 px-3 border-x-2 border-[#0ff] rounded-full hover:shadow-sm-neon transition-slow-1 relative z-10 py-[1rem] text-center text-lg'>
                        Bio
                    </Link>
                </SheetDescription>
            </SheetContent>
        </Sheet>
    )
}

export default MobileNavDEV