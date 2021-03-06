# CustomerPreferences

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blacklisted_emails** | **dict(str, int)** | List of blacklisted emails of the customer | [optional] 
**created_epoch_millis** | **int** |  | [optional] 
**creator_id** | **str** |  | [optional] 
**customer_id** | **str** | The id of the customer preferences are attached to | 
**default_user_groups** | [**list[UserGroup]**](UserGroup.md) | List of default user groups of the customer | [optional] 
**deleted** | **bool** |  | [optional] 
**grant_modify_access_to_everyone** | **bool** | Whether modify access of new entites is granted to Everyone or to the Creator | 
**hidden_metric_prefixes** | **dict(str, int)** | Metric prefixes which should be hidden from user | [optional] 
**hide_ts_when_querybuilder_shown** | **bool** | Whether to hide TS source input when Querybuilder is shown | 
**id** | **str** |  | [optional] 
**invite_permissions** | **list[str]** | List of permissions that are assigned to newly invited users | [optional] 
**landing_dashboard_slug** | **str** | Dashboard where user will be redirected from landing page | [optional] 
**show_onboarding** | **bool** | Whether to show onboarding for any new user without an override | 
**show_querybuilder_by_default** | **bool** | Whether the Querybuilder is shown by default | 
**updated_epoch_millis** | **int** |  | [optional] 
**updater_id** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


