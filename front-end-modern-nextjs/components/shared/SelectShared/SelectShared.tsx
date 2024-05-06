
import React from 'react'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'

const SelectDEV = ({
    placeholder = 'Theme',
    items = ['light', 'dark', 'system'],
    className = '',
    onValueChange = (value: string) => { }
}) => {
    return (
        <>
            <Select onValueChange={onValueChange}>
                <SelectTrigger className={`w-full bg-bgprimary border-[#0ff] relative z-10 ${className}`}>
                    {placeholder}
                </SelectTrigger>
                <SelectContent className='bg-bgprimary border-[#0ff]'>
                    {items.map((item, index) => {
                        return <SelectItem className='bg-bgsecondary focus:bg-black hover:shadow-sm-neon transition-all duration-150 ease-in-out mb-2' key={index} value={item}>{item}</SelectItem>
                    })}
                </SelectContent>
            </Select>

        </>
    )
}

export default SelectDEV