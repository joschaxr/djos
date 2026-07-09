import { useEffect, useState } from "react"
import { apiGet } from "../api/client"
import type { Track } from "../types/track"

export function useTracks() {
  const [tracks, setTracks] = useState<Track[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    apiGet<Track[]>("/tracks")
      .then(setTracks)
      .finally(() => setLoading(false))
  }, [])

  return {
    tracks,
    loading,
  }
}