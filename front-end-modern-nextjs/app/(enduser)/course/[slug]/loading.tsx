

export default function LessonOfCourseLoading() {
    // Or a custom loading skeleton component
    return <>
        <p className='text-xl border-l-2 border-b-2 border-[#0ff] w-fit px-5 py-2 rounded-xl mb-5'>Bài Học</p>
        <div className=''>
            {Array.from({ length: 10 }).map((_, index: number) => {
                return <div key={index} className="neon-loading mb-4">
                    <div className="neon-pulse"></div>
                </div>
            })}
        </div>
    </>
}