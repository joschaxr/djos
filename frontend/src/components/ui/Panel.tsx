import type { ReactNode } from "react"

type Props = {
  children: ReactNode
  className?: string
}

export default function Panel({ children, className = "" }: Props) {
  return (
    <div
      className={`
        rounded-2xl
        border
        border-slate-800
        bg-slate-900/70
        p-5
        shadow-xl
        ${className}
      `}
    >
      {children}
    </div>
  )
}