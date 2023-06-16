from app.filters.filter_education_insight import FilterEducationInsight


class Filters:
    @staticmethod
    def addFilters(filters, form_data):

        if filters.get("education_insight"):
            FilterEducationInsight.add_education_insight_filter(filters["experience"], form_data)

