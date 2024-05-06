import React from 'react'

const Section = ({
  children,
  id='home'
}: {
  children: React.ReactNode,
  id?: string
}) => {
  return (
    <div id={id} className='container mx-auto flex justify-cente min-h-screen h-auto lg:pt-[6rem] pt-5'>
      {children}
    </div>
  )
}

export default Section