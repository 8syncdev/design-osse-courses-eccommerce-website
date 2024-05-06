import lessonService from '@/src/server/service/lesson.action'
import React from 'react'
import MarkDownDEV from '@/components/comp_dev/MarkDownDEV/MarkDownDEV';


const LessonDetailCourse = async ({
  lesson_id
}: {
  lesson_id: number
}) => {
  const data = await lessonService.getLessonDetail(lesson_id)

  return (
    <div>
      {data && data?.content && (
        <div>
          <MarkDownDEV content={data.content} />
        </div>
      
      )}
    </div>
  )
}

export default LessonDetailCourse

