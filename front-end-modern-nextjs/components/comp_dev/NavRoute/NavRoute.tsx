'use client'

import { Button } from '@/components/ui/button'
import { usePathname, useRouter } from 'next/navigation'

import React from 'react'

const NavRoute = () => {
  const pathName = usePathname()
  const router = useRouter()

  return (
    <div className='container mx-auto'>
      {pathName != '/' && (
        <div className='py-2'>
          <Button onClick={() => router.back()} className='relative z-10'>
            Quay lại
          </Button>
        </div>
      )}
    </div>
  )
}

export default NavRoute