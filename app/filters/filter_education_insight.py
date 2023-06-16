from app.repository.Elastic import ElasticQuery
from utils.common.constant.SearchScope import SearchScope


class FilterEducationInsight:

    @classmethod
    def add_education_insight_filter(cls, filter_com, filter_list):

        if filter_com.get("achiever"):
            filter_list.append(
                ElasticQuery.generateTermQuery(filter_com.get("achiever"),
                                               SearchScope.get_field("achiever"))
            )

        if filter_com.get("bits_grad"):
            filter_list.append(
                ElasticQuery.generateTermQuery(SearchScope.get_field("bits_grad"),
                                               filter_com.get("bits_grad"))
            )

        if filter_com.get("fast_phd"):
            filter_list.append(
                ElasticQuery.generateTermQuery(SearchScope.get_field("fast_phd"),
                                               filter_com.get("fast_phd"))
            )

        if filter_com.get("from_prestigious_college"):
            filter_list.append(
                ElasticQuery.generateTermQuery(SearchScope.get_field("from_prestigious_college"),
                                               filter_com.get("from_prestigious_college"))
            )

        if filter_com.get("iim_grad"):
            filter_list.append(
                ElasticQuery.generateTermQuery(SearchScope.get_field("iim_grad"),
                                               filter_com.get("iim_grad"))
            )

        if filter_com.get("iit_grad"):
            filter_list.append(
                ElasticQuery.generateTermQuery(SearchScope.get_field("iit_grad"),
                                               filter_com.get("iit_grad"))
            )

        if filter_com.get("is_associate"):
            filter_list.append(
                ElasticQuery.generateTermQuery(SearchScope.get_field("is_associate"),
                                               filter_com.get("is_associate"))
            )

        if filter_com.get("is_bachelor"):
            filter_list.append(
                ElasticQuery.generateTermQuery(SearchScope.get_field("is_bachelor"),
                                               filter_com.get("is_bachelor"))
            )

        if filter_com.get("is_master"):
            filter_list.append(
                ElasticQuery.generateTermQuery(SearchScope.get_field("is_master"),
                                               filter_com.get("is_master"))
            )

        if filter_com.get("is_phd"):
            filter_list.append(
                ElasticQuery.generateTermQuery(SearchScope.get_field("is_phd"),
                                               filter_com.get("is_phd"))
            )

        if filter_com.get("is_post_doc"):
            filter_list.append(
                ElasticQuery.generateTermQuery(SearchScope.get_field("is_post_doc"),
                                               filter_com.get("is_post_doc"))
            )

        if filter_com.get("major_bucket"):
            filter_list.append(
                ElasticQuery.generateTermQuery(SearchScope.get_field("major_bucket"),
                                               filter_com.get("major_bucket"))
            )

        if filter_com.get("nit_grad"):
            filter_list.append(
                ElasticQuery.generateTermQuery(SearchScope.get_field("nit_grad"),
                                               filter_com.get("nit_grad"))
            )

        if filter_com.get("recent_grad"):
            filter_list.append(
                ElasticQuery.generateTermQuery(SearchScope.get_field("education_insight_recent_grad"),
                                               filter_com.get("recent_grad"))
            )

        if filter_com.get("tier1_college_grad"):
            filter_list.append(
                ElasticQuery.generateTermQuery(SearchScope.get_field("tier1_college_grad"),
                                               filter_com.get("tier1_college_grad"))
            )

        if filter_com.get("top200_college_grad"):
            filter_list.append(
                ElasticQuery.generateTermQuery(SearchScope.get_field("top200_college_grad"),
                                               filter_com.get("top200_college_grad"))
            )

        if filter_com.get("top_qualification_name"):
            filter_list.append(
                ElasticQuery.generateTermQuery(SearchScope.get_field("top_qualification_name"),
                                               filter_com.get("top_qualification_name"))
            )

        if filter_com.get("top_qualification_year"):
            filter_list.append(
                ElasticQuery.generateTermQuery(SearchScope.get_field("top_qualification_year"),
                                               filter_com.get("top_qualification_year"))
            )
        if filter_com.get("world_top_college_grad"):
            filter_list.append(
                ElasticQuery.generateTermQuery(SearchScope.get_field("world_top_college_grad"),
                                               filter_com.get("world_top_college_grad"))
            )

        return filter_list
