import React from 'react'
import './Background.scss'
const Background = () => {
  return (
    <div className='stars'>
      {Array.from(Array(20).keys()).map((i) => (
        <div key={i} className='star'></div>
      ))}
    </div>
  )
}

export default Background