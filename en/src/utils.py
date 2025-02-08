# utils.py - Helper functions for Virtual Pop Idols AI project

def calculate_audience_engagement(feedback_log):
    """Calculates audience engagement level based on feedback."""
    positive_feedback = feedback_log.count("positive")
    neutral_feedback = feedback_log.count("neutral")
    negative_feedback = feedback_log.count("negative")

    total_feedback = positive_feedback + neutral_feedback + negative_feedback
    if total_feedback == 0:
        return 0

    engagement_score = (positive_feedback - negative_feedback) / total_feedback * 100
    return round(engagement_score, 2)

def display_performance_summary(idol_name, feedback_log):
    """Displays a performance summary for the AI idol."""
    engagement_score = calculate_audience_engagement(feedback_log)
    print(f"\n--- Performance Summary for {idol_name} ---")
    print(f"Audience Engagement Score: {engagement_score}%")
    print(f"Total Feedback Collected: {len(feedback_log)}")
    print("Feedback Breakdown:")
    print(f"- Positive: {feedback_log.count('positive')}")
    print(f"- Neutral: {feedback_log.count('neutral')}")
    print(f"- Negative: {feedback_log.count('negative')}")
    print("-----------------------------------------\n")
