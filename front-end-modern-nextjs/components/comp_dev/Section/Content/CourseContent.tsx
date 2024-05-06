import React from 'react'
import Section from '../Section'
import { courseService } from '@/src/server'
import { Button } from '@/components/ui/button'
import Image from 'next/image'
import { convertDate, getImageUtil } from '@/src/utils'
import Link from 'next/link'
import { ResponseCoursesAPIType } from '@/types'
import LoadingBar from '../../LoadingStateDEV/LoadingBar'

const CourseContent = async () => {
    // Set { initializeWithValue: false } in SSR context
    // console.log(value)
    let data: any[] = []
    data = await courseService.getCourse()

    

    return (
        <>
            <div className='flex flex-col gap-5'>
                {data ? data.length > 0 && data.map((item: ResponseCoursesAPIType, index) => {
                    return <div key={index} className='w-full border-2 rounded-md border-[#0ff] flex items-center p-3 flex-wrap md:flex-nowrap'>
                        <div className="flip-card relative z-10 w-full cursor-pointer overflow-hidden">
                            <div className="flip-card-inner">
                                <div className="flip-card-front flex items-center gap-3 relative">
                                    <Image src={getImageUtil(item?.title)} alt='' className='' />
                                    <div>
                                        <h2>Khóa Học: {item?.title}</h2>
                                        <p>Giáo Viên: {item?.instructor_name.length>5?item.instructor_name:'Admin 8SyncDev'}</p>
                                    </div>
                                    <span className='absolute top-0 right-7 border-2 p-1 text-sm rounded-full border-[#0ff]'>{convertDate(item?.created_at).split(' ').slice(1, 4).join('-')}</span>
                                </div>
                                <div className="flip-card-back flex items-center">
                                    <p className='px-5'>{item?.description}</p>
                                </div>
                            </div>
                        </div>
                        <div>
                            <Button className='h-[3.5rem] px-10 text-xl'>
                                <Link href={{
                                    pathname: `/course/${item?.slug}`, // * Because of the slug make more sense than id
                                    query: { 
                                        id: item?.id,
                                     }
                                }}>
                                    Vào Học
                                </Link>
                            </Button>
                        </div>
                    </div>
                }): <>
                    <LoadingBar />
                </>}
            </div>
        </>
    )
}

export default CourseContent