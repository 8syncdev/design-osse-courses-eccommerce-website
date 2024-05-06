import React from 'react'

const LoadingLayoutEndUser = () => {
  return (
    <div className='container mx-auto flex justify-center h-full lg:pt-[6rem] pt-5'>
      <div className='w-full'>
        <div className='grid grid-cols-12 lg:pb-20 pb-5 w-full'>
          <div className="lg:col-span-6 col-span-12 lg:mb-0 mb-20">
            <div className='font-[550] lg:text-[2rem] text-[1.2rem]' />
            <div className='neon-loading'>
              <div className="neon-pulse mb-4 h-[50px]"></div>
              <div className="neon-pulse mb-4 h-[50px]"></div>
              <div className="neon-pulse mb-4 h-[50px]"></div>
              <div className="neon-pulse mb-4 h-[50px]"></div>
              <div className="neon-pulse mb-4 h-[50px]"></div>
            </div>

          </div>
          <div className="lg:col-span-6 col-span-12 pl-10 overflow-hidden">
            <div className='neon-loading'>
              <div className="neon-pulse mb-4 h-[300px]"></div>
            </div>
          </div>
        </div>
        <div>
          <div className='neon-loading'>
            <div className="neon-pulse mb-4 h-[50px]"></div>
            <div className="neon-pulse mb-4 h-[50px]"></div>
            <div className="neon-pulse mb-4 h-[50px]"></div>
            <div className="neon-pulse mb-4 h-[50px]"></div>
            <div className="neon-pulse mb-4 h-[50px]"></div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default LoadingLayoutEndUser