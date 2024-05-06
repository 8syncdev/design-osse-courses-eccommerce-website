import React from 'react'
import Section from '../Section'
import SlidePicDEV from '../../SlidePicDEV/SlidePicDEV'
import TypeWriterDEV from '../../TypeWriteDEV/TypeWriteDEV'
import AnimatedWordDEV from '../../AnimatedWord/AnimatedWordDEV'

const HomeContent = () => {
  return (
    <Section>
      <div>
        <div className='grid grid-cols-12 lg:pb-32 pb-5'>
          <div className="lg:col-span-6 col-span-12 lg:mb-0 mb-20">
            <TypeWriterDEV className='font-[550] lg:text-[2rem] text-[1.2rem]' />
            <p className='text-lg'>Chào các bạn đã đến với trang web của mình. Mình là một lập trình viên fullstack. Mình sẽ chia sẻ kiến thức và kinh nghiệm của mình qua các bài viết trên trang web này. Mình hy vọng rằng các bạn sẽ học được nhiều điều từ trang web này. Chúc các bạn học tốt!
            </p>
          </div>
          <div className="lg:col-span-6 col-span-12 pl-10 overflow-hidden">
            <SlidePicDEV />
          </div>
        </div>
        <AnimatedWordDEV />
      </div>
    </Section>
  )
}

export default HomeContent