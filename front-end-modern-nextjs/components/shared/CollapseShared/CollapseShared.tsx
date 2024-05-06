"use client"
import React, { memo } from 'react'
import { Collapsible, CollapsibleContent, CollapsibleTrigger } from '@/components/ui/collapsible'
import { Plus, Minus, ArrowDown } from 'lucide-react'
import { Button } from '@/components/ui/button'



const CollapseShared = ({
    name = "CollapseDEV",
    className = "",
    children = <></>,
    IconOpen = Plus,
    IconClose = Minus,
    IconArrow = ArrowDown,
    arrow = true,
    isBlur = true,
    open = false,
    premium = false
}) => {
    const [isOpen, setIsOpen] = React.useState(open)

    return (
        <div>
            <Collapsible
                open={isOpen}
                onOpenChange={setIsOpen}
                className={`p-3 bg-bgsecondary/50 rounded-md border-2 border-[#0ff] relative z-10 ${className}`}
            >
                <CollapsibleTrigger className='w-full'>
                    <div className='flex justify-between'>
                        <p className='font-[550] text-lg'>{name}</p>
                        <div className='flex gap-3 items-center'>
                            <span className='text-sm text-neon'>{premium?'PREMIUM':'Miễn Phí'}</span>
                            {arrow ? <>
                                <IconArrow className={`transition-all duration-300 ${isOpen ? 'rotate-180' : 'rotate-0'}`} />
                            </> : <></>}
                        </div>
                    </div>
                </CollapsibleTrigger>
                <hr className='my-3' />

                <CollapsibleContent>
                    {children}
                </CollapsibleContent>
                {/* Blur Content  */}
                {isBlur && <>
                    <div className='h-[6rem] overflow-hidden relative'>
                        {!isOpen && children}
                        <div className={`${!isOpen ? 'absolute bottom-0 left-0 backdrop-blur-sm' : ''} w-full bg-black/5 rounded-md p-2 flex justify-center`}>
                            <CollapsibleTrigger className='neon-button w-[15rem] rounded-full'>
                                {isOpen ? 'Thu gọn' : 'Xem thêm'}
                            </CollapsibleTrigger>
                        </div>
                    </div>
                </>}

            </Collapsible>
        </div>
    )
}

export default memo(CollapseShared)