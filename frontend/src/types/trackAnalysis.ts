export interface TrackAnalysisPayload {
  track: {
    id: number
    artist: string
    title: string
    duration_ms: number | null
    image_url: string | null
  }

  analysis: {
    bpm: number | null
    musical_key: number | null
    mode: number | null
    camelot_key: string | null
  }

  beats: Array<{
    beat_index: number
    time_seconds: number
  }>

  bars: Array<{
    bar_index: number
    start_time: number
    end_time: number | null
  }>

  phrases: Array<{
    phrase_index: number
    start_time: number
    end_time: number | null
    bars_count: number | null
  }>

  change_points: Array<{
    index: number
    score: number
  }>
}