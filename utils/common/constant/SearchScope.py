class SearchScope:
    FIELD_MAP = {
        "achiever": "education_insight.achiever.value",
        "bits_grad": "education_insight.bits_grad.value",
        "fast_phd": "education_insight.fast_phd.value",
        "from_prestigious_college": "education_insight.from_prestigious_college.value",
        "iim_grad": "education_insight.iim_grad.value",
        "iit_grad": "education_insight.iit_grad.value",
        "is_associate": "education_insight.is_associate.value",
        "is_bachelor": "education_insight.is_bachelor.value",
        "is_master": "education_insight.is_master.value",
        "is_phd": "education_insight.is_phd.value",
        "is_post_doc": "education_insight.is_post_doc.value",
        "major_bucket": "education_insight.major_bucket.value",  # remove
        "nit_grad": "education_insight.nit_grad.value",
        "education_insight_recent_grad": "education_insight.recent_grad.value",  # duplicate already exists [ recent_grad ]
        "tier1_college_grad": "education_insight.tier1_college_grad.value",
        "top200_college_grad": "education_insight.top200_college_grad.value",
        "top_qualification_name": "education_insight.top_qualification_name.value",
        "top_qualification_year": "education_insight.top_qualification_year.value",
        "world_top_college_grad": "education_insight.world_top_college_grad.value",
    }

    def get_field(self, value):
        return self.FIELD_MAP.get(value)


SearchScope = SearchScope()
