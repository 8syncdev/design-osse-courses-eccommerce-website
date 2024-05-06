'use client'
import RegisterAlertShared from '@/components/shared/AlertShared/RegisterAlertShared'
import Link from 'next/link'
import React from 'react'
import MobileNavDEV from './MobileNavDEV'
import AuthAvatarProvider from '@/src/provider/AuthAvatarProvider'

const HeaderDEV = () => {
  return (
    <header className='neon-blind relative z-10'>
      <div className="flex justify-between items-center container mx-auto">
        <div className='lg:hidden block relative z-10'>
          <MobileNavDEV />
        </div>
        <div className='lg:flex gap-3 hidden'>
          <Link href='/' className='border-b-2 px-3 border-x-2 border-[#0ff] rounded-full hover:shadow-sm-neon transition-slow-1 relative z-10 py-[0.15rem]'>
            Home
          </Link>
          <Link href='/course' className='border-b-2 px-3 border-x-2 border-[#0ff] rounded-full hover:shadow-sm-neon transition-slow-1 relative z-10 py-[0.15rem]'>
            Khóa học
          </Link>
          <Link href='/' className='border-b-2 px-3 border-x-2 border-[#0ff] rounded-full hover:shadow-sm-neon transition-slow-1 relative z-10 py-[0.15rem]'>
            About
          </Link>
          <Link href='/' className='border-b-2 px-3 border-x-2 border-[#0ff] rounded-full hover:shadow-sm-neon transition-slow-1 relative z-10 py-[0.15rem]'>
            Bio
          </Link>
        </div>
        <div className='h-[6rem] grid items-center'>
          <AuthAvatarProvider>
            <RegisterAlertShared />
          </AuthAvatarProvider>
        </div>
      </div>
    </header>
  )
}

export default HeaderDEV