'use client'
import React from 'react'
import { useParams, usePathname } from 'next/navigation'
import { useSearchParams } from 'next/navigation'









const TransitionProvider = ({
  children
}: {
  children: React.ReactNode
}) => {
  const pathName = usePathname()
  // console.log(pathName)
  const _useSearchParams = useSearchParams()
  // console.log(_useSearchParams?.get('authToken'))
  if (_useSearchParams?.get('authToken') && pathName == '/') {
    localStorage.setItem('authToken', (_useSearchParams?.get('authToken')) as string)
    // sessionStorage.setItem('authToken', (_useSearchParams?.get('authToken')))
  }

  return (
    <main className='h-full'>
      {children}
    </main>
  )
}

export default TransitionProvider


