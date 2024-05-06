import React from 'react'
import Markdown from "markdown-to-jsx";
import SyntaxHighlighter from 'react-syntax-highlighter';
import { docco } from 'react-syntax-highlighter/dist/esm/styles/hljs';
import { dark, dracula } from 'react-syntax-highlighter/dist/esm/styles/prism';




const MarkDownDEV = ({
    content
}: {
    content: string
}) => {
  return (
      <Markdown
          options={{
              overrides: {
                  code: SyntaxHighlightedCode,
                  h1: { component: 'h1', props: { className: 'text-2xl font-bold mb-7 shadow-sm-neon p-2 rounded-md w-fit' } },
                  h2: { component: 'h2', props: { className: 'text-xl font-bold my-5 border-b-2 border-[#0ff] p-2 w-fit rounded-md' } },
                  p: { component: 'p', props: { className: '' } },
                  li: { component: 'li', props: { className: 'pl-5 border-l-2' } },

              }
          }}
      >
          {content}
      </Markdown>
  )
}

export default MarkDownDEV


const SyntaxHighlightedCode = ({ children }: { children: string }) => {
    return (
        <SyntaxHighlighter language="python" style={dark}>
            {children}
        </SyntaxHighlighter>
    )
}