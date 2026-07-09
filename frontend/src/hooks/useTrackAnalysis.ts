import { useEffect, useState } from "react"

import { apiGet } from "../api/client"
import type { TrackAnalysisPayload } from "../types/trackAnalysis"

export function useTrackAnalysis(trackId: number | null) {
  const [analysis, setAnalysis] =
    useState<TrackAnalysisPayload | null>(null)

  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    if (!trackId) {
      setAnalysis(null)
      setError(null)
      return
    }

    setLoading(true)
    setAnalysis(null)
    setError(null)

    apiGet<TrackAnalysisPayload>(`/tracks/${trackId}/analysis`)
      .then((data) => {
        console.log("Track analysis loaded:", data)
        setAnalysis(data)
      })
      .catch((error) => {
        console.error("Track analysis error:", error)
        setError(String(error))
        setAnalysis(null)
      })
      .finally(() => setLoading(false))
  }, [trackId])

  return {
    analysis,
    loading,
    error,
  }
}