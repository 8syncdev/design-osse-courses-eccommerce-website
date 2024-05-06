import LoadingBar from '@/components/comp_dev/LoadingStateDEV/LoadingBar'
import CollapseItemShared from '@/components/shared/CollapseShared/CollapseItemShared'
import CollapseShared from '@/components/shared/CollapseShared/CollapseShared'
import { courseService } from '@/src/server'
import { CourseType } from '@/types/response'
// import { CourseType, DetailLessonType } from '@/types/response'
import Link from 'next/link'
import React from 'react'

const LessonOfCourseDetail = async ({
    course_id,
    params,
    searchParams
}: {
    course_id: number,
    params?: { slug: string },
    searchParams?: any
}) => {
    let data = await courseService.getCourseDetail(course_id)
    return (
        <>
            <div className='flex flex-col gap-4'>
                {data ? data?.results.map((item: CourseType, index: number) => {
                    return <CollapseShared key={index} name={item.name} isBlur={index === 1 ? true : false} premium={index>0 ? true : false} open={index===0?true:false}>
                        <>
                            <CollapseItemShared id={item.id} />
                        </>
                    </CollapseShared>
                }) : <>
                    <LoadingBar />
                </>}
            </div>
        </>
    )
}

export default LessonOfCourseDetail