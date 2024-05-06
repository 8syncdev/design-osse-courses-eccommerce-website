import LessonOfCourseDetail from '@/components/comp_dev/Section/Content/Detail/LessonOfCourseDetail'
import React from 'react'

const CoursDetailLesson = ({ params, searchParams }: { 
  params: { slug: string },
  searchParams: any
}) => {
  console.log(params, searchParams)
  return (
      <>
      <LessonOfCourseDetail course_id={Number(searchParams?.id)} searchParams={searchParams}/>
      </>
  )
}

export default CoursDetailLesson