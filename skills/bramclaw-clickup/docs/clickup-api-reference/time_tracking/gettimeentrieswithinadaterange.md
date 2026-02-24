# Get time entries within a date range

View time entries filtered by start and end date. \
 \
By default, this endpoint returns time entries from the last 30 days created by the authenticated user. \
 \
To retrieve time entries for other users, you must include the `assignee` query parameter. \
 \
Only one of the following location filters can be included at a time: `space_id`, `folder_id`, `list_id`, or `task_id`. \
 \
***Note:** A time entry that has a negative duration means that timer is currently running for that user.*

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "ClickUp API v2 Reference",
    "description": "The ClickUp API enables you to programmatically access and manage your ClickUp resources.\n\n## Authentication\nThe API supports two authentication methods:\n- **Personal API Token**: Use for testing and personal integrations. Add token to requests with header: `Authorization: pk_...`\n- **OAuth 2.0**: Required for building apps for other users. Uses authorization code flow.\n\n## Getting Started\nOur [Getting Started Guide](https://developer.clickup.com/docs/index) provides a comprehensive overview of how to use the ClickUp API.\n",
    "contact": {},
    "version": "2.0"
  },
  "jsonSchemaDialect": "https://json-schema.org/draft/2020-12/schema",
  "servers": [
    {
      "url": "https://api.clickup.com/api",
      "description": "ClickUp",
      "variables": {}
    }
  ],
  "paths": {
    "/v2/team/{team_Id}/time_entries": {
      "get": {
        "summary": "Get time entries within a date range",
        "tags": [
          "Time Tracking"
        ],
        "description": "View time entries filtered by start and end date. \\\n \\\nBy default, this endpoint returns time entries from the last 30 days created by the authenticated user. \\\n \\\nTo retrieve time entries for other users, you must include the `assignee` query parameter. \\\n \\\nOnly one of the following location filters can be included at a time: `space_id`, `folder_id`, `list_id`, or `task_id`. \\\n \\\n***Note:** A time entry that has a negative duration means that timer is currently running for that user.*",
        "operationId": "Gettimeentrieswithinadaterange",
        "parameters": [
          {
            "name": "team_Id",
            "in": "path",
            "description": "Workspace ID",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                123
              ]
            }
          },
          {
            "name": "start_date",
            "in": "query",
            "description": "Unix time in milliseconds",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "number",
              "contentEncoding": "double"
            }
          },
          {
            "name": "end_date",
            "in": "query",
            "description": "Unix time in milliseconds",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "number",
              "contentEncoding": "double"
            }
          },
          {
            "name": "assignee",
            "in": "query",
            "description": "Filter by `user_id`. For multiple assignees, separate `user_id` using commas.\\\n \\\n **Example:** `assignee=1234,9876`\\\n \\\n***Note:** Only Workspace Owners/Admins have access to do this.*",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "number",
              "contentEncoding": "double"
            }
          },
          {
            "name": "include_task_tags",
            "in": "query",
            "description": "Include task tags in the response for time entries associated with tasks.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "include_location_names",
            "in": "query",
            "description": "Include the names of the List, Folder, and Space along with the `list_id`,`folder_id`, and `space_id`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "include_approval_history",
            "in": "query",
            "description": "Include the history of the approval for each time entry. Adds status changes, notes, and approvers.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "include_approval_details",
            "in": "query",
            "description": "Include the details of the approval for each time entry. Adds Approver ID, Approved Time, List of Approvers, and Approval Status.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "space_id",
            "in": "query",
            "description": "Only include time entries associated with tasks in a specific Space.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "number",
              "contentEncoding": "double"
            }
          },
          {
            "name": "folder_id",
            "in": "query",
            "description": "Only include time entries associated with tasks in a specific Folder.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "number",
              "contentEncoding": "double"
            }
          },
          {
            "name": "list_id",
            "in": "query",
            "description": "Only include time entries associated with tasks in a specific List.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "number",
              "contentEncoding": "double"
            }
          },
          {
            "name": "task_id",
            "in": "query",
            "description": "Only include time entries associated with a specific task.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "custom_task_ids",
            "in": "query",
            "description": "If you want to reference a task by it's custom task id, this value must be `true`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean",
              "examples": [
                true
              ]
            }
          },
          {
            "name": "team_id",
            "in": "query",
            "description": "When the `custom_task_ids` parameter is set to `true`, the Workspace ID must be provided using the `team_id` parameter.\n \\\nFor example: `custom_task_ids=true&team_id=123`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                123
              ]
            }
          },
          {
            "name": "is_billable",
            "in": "query",
            "description": "Include only billable time entries by using a value of `true` or only non-billable time entries by using a value of `false`.\\\n \\\nFor example: `?is_billable=true`.",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "boolean",
              "examples": [
                true
              ]
            }
          },
          {
            "name": "Content-Type",
            "in": "header",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "const": "application/json",
              "type": "string",
              "examples": [
                "application/json"
              ]
            }
          }
        ],
        "responses": {
          "200": {
            "description": "If your time entry is associated with a task that uses custom task ids you can expect a `custom_id`` field in the body of the response. The task field will only be included if there is a task associated with a time entry.",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "Gettimeentrieswithinadaterangeresponse",
                  "required": [
                    "data"
                  ],
                  "type": "object",
                  "properties": {
                    "data": {
                      "type": "array",
                      "items": {
                        "title": "Datum1",
                        "required": [
                          "id",
                          "task",
                          "wid",
                          "user",
                          "billable",
                          "start",
                          "end",
                          "duration",
                          "description",
                          "tags",
                          "source",
                          "at",
                          "task_location",
                          "task_tags",
                          "task_url"
                        ],
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string"
                          },
                          "task": {
                            "title": "Task4",
                            "required": [
                              "id",
                              "custom_id",
                              "name",
                              "status",
                              "custom_type"
                            ],
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string"
                              },
                              "custom_id": {
                                "type": "string"
                              },
                              "name": {
                                "type": "string"
                              },
                              "status": {
                                "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/status"
                              },
                              "custom_type": {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              }
                            },
                            "examples": [
                              {
                                "id": "1vwwavv",
                                "custom_id": "JOSH-917",
                                "name": "woof",
                                "status": {
                                  "status": "open yes",
                                  "color": "#d3d3d3",
                                  "type": "open",
                                  "orderindex": 0
                                },
                                "custom_type": null
                              }
                            ]
                          },
                          "wid": {
                            "type": "string"
                          },
                          "user": {
                            "$ref": "#/paths/~1v2~1team~1%7Bteam_id%7D~1time_entries~1stop/post/responses/200/content/application~1json/schema/properties/data/properties/user"
                          },
                          "billable": {
                            "type": "boolean"
                          },
                          "start": {
                            "type": "string"
                          },
                          "end": {
                            "type": "string"
                          },
                          "duration": {
                            "type": "string"
                          },
                          "description": {
                            "type": "string"
                          },
                          "tags": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            },
                            "description": ""
                          },
                          "source": {
                            "type": "string"
                          },
                          "at": {
                            "type": "string"
                          },
                          "approval_id": {
                            "type": "string",
                            "description": "ID of the associated approval"
                          },
                          "approval": {
                            "$ref": "#/paths/~1v2~1team~1%7Bteam_Id%7D~1time_entries/get/responses/200/content/application~1json/schema/examples/0/data/0/approval"
                          },
                          "task_location": {
                            "$ref": "#/paths/~1v2~1team~1%7Bteam_id%7D~1time_entries~1%7Btimer_id%7D/get/responses/200/content/application~1json/schema/properties/data/properties/task_location"
                          },
                          "task_tags": {
                            "type": "array",
                            "items": {
                              "$ref": "#/paths/~1v2~1team~1%7Bteam_id%7D~1time_entries~1%7Btimer_id%7D/get/responses/200/content/application~1json/schema/properties/data/properties/task_tags/items"
                            },
                            "description": ""
                          },
                          "task_url": {
                            "type": "string"
                          }
                        },
                        "examples": [
                          {
                            "id": "1963465985517105840",
                            "task": {
                              "id": "1vwwavv",
                              "custom_id": "JOSH-917",
                              "name": "woof",
                              "status": {
                                "status": "open yes",
                                "color": "#d3d3d3",
                                "type": "open",
                                "orderindex": 0
                              },
                              "custom_type": null
                            },
                            "wid": "300702",
                            "user": {
                              "id": 1,
                              "username": "first_name last_name",
                              "email": "test@gmail.com",
                              "color": "#08c7e0",
                              "initials": "JK",
                              "profilePicture": "https://attachments.clickup.com/profilePictures/1_HHk.jpg"
                            },
                            "billable": false,
                            "start": "1592841559129",
                            "end": "1592845899021",
                            "duration": "4339892",
                            "description": "",
                            "tags": [],
                            "source": "clickup",
                            "at": "1592845899021",
                            "approval_id": "2d539936-119a-4927-9770-179f0a72e2e5",
                            "approval": {
                              "$ref": "#/paths/~1v2~1team~1%7Bteam_Id%7D~1time_entries/get/responses/200/content/application~1json/schema/examples/0/data/0/approval"
                            },
                            "task_location": {
                              "list_id": 1560300071,
                              "folder_id": 468300080,
                              "space_id": 22800253,
                              "list_name": "List",
                              "folder_name": "Folder",
                              "space_name": "Space"
                            },
                            "task_tags": [
                              {
                                "name": "content-request",
                                "tag_fg": "#800000",
                                "tag_bg": "#2ecd6f",
                                "creator": 301828
                              },
                              {
                                "name": "marketing-okr",
                                "tag_fg": "#800000",
                                "tag_bg": "#7C4DFF",
                                "creator": 301828
                              }
                            ],
                            "task_url": "https://staging.clickup.com/t/1vwwavv"
                          }
                        ]
                      },
                      "description": ""
                    }
                  },
                  "examples": [
                    {
                      "data": [
                        {
                          "id": "1963465985517105840",
                          "task": {
                            "id": "1vwwavv",
                            "custom_id": "JOSH-917",
                            "name": "woof",
                            "status": {
                              "status": "open yes",
                              "color": "#d3d3d3",
                              "type": "open",
                              "orderindex": 0
                            },
                            "custom_type": null
                          },
                          "wid": "300702",
                          "user": {
                            "id": 1,
                            "username": "first_name last_name",
                            "email": "test@gmail.com",
                            "color": "#08c7e0",
                            "initials": "JK",
                            "profilePicture": "https://attachments.clickup.com/profilePictures/1_HHk.jpg"
                          },
                          "billable": false,
                          "start": 1592841559129,
                          "end": 1592845899021,
                          "duration": "4339892",
                          "description": "",
                          "tags": [],
                          "source": "clickup",
                          "at": "1592845899021",
                          "approval_id": "2d539936-119a-4927-9770-179f0a72e2e5",
                          "approval": {
                            "title": "Approval",
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string",
                                "description": "Unique identifier for the approval"
                              },
                              "workspace_id": {
                                "type": "integer",
                                "description": "ID of the workspace this approval belongs to"
                              },
                              "status": {
                                "type": "string",
                                "description": "Current status of the approval (e.g., 'approved', 'pending')"
                              },
                              "data": {
                                "type": "object",
                                "properties": {
                                  "end_of_week": {
                                    "type": "integer",
                                    "description": "Timestamp for the end of the week"
                                  },
                                  "start_of_week": {
                                    "type": "integer",
                                    "description": "Timestamp for the start of the week"
                                  }
                                }
                              },
                              "user": {
                                "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D~1time/get/responses/200/content/application~1json/schema/properties/data/items/properties/user"
                              },
                              "approvers": {
                                "type": "array",
                                "items": {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "integer",
                                      "description": "ID of the user who can approve the request"
                                    }
                                  }
                                }
                              },
                              "approver_id": {
                                "type": "integer",
                                "description": "ID of the user who approved the request"
                              },
                              "approved_at": {
                                "type": "integer",
                                "description": "Timestamp when the approval was granted"
                              },
                              "history": {
                                "type": "array",
                                "items": {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      "type": "string",
                                      "description": "Unique identifier for the history entry"
                                    },
                                    "field": {
                                      "type": "string",
                                      "description": "Field that was changed"
                                    },
                                    "before": {
                                      "type": "string",
                                      "description": "Previous value"
                                    },
                                    "after": {
                                      "type": "string",
                                      "description": "New value"
                                    },
                                    "created_at": {
                                      "type": "integer",
                                      "description": "Timestamp when the change was made"
                                    },
                                    "user": {
                                      "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D~1time/get/responses/200/content/application~1json/schema/properties/data/items/properties/user"
                                    }
                                  }
                                }
                              }
                            },
                            "examples": [
                              {
                                "id": "123e4567-e89b-12d3-a456-426614174000",
                                "workspace_id": 12345,
                                "status": "approved",
                                "data": {
                                  "end_of_week": 1672531199000,
                                  "start_of_week": 1671926400000
                                },
                                "user": {
                                  "id": 101,
                                  "username": "john.smith",
                                  "initials": "JS",
                                  "avatar": {
                                    "color": "#4287f5",
                                    "picture_url": null
                                  }
                                },
                                "approvers": [
                                  {
                                    "id": 101
                                  },
                                  {
                                    "id": 102
                                  }
                                ],
                                "approver_id": 101,
                                "approved_at": 1672012800000,
                                "history": [
                                  {
                                    "id": "987fcdeb-51a2-3456-789a-bcdef0123456",
                                    "field": "submission",
                                    "before": null,
                                    "after": null,
                                    "created_at": 1671987600000,
                                    "user": {
                                      "id": 101,
                                      "username": "john.smith",
                                      "role": "submitter"
                                    }
                                  },
                                  {
                                    "id": "456abcde-f123-4567-89ab-cdef01234567",
                                    "field": "status",
                                    "before": "pending",
                                    "after": "approved",
                                    "created_at": 1672012800000,
                                    "user": {
                                      "id": 102,
                                      "username": "jane.doe",
                                      "role": "approver"
                                    }
                                  }
                                ]
                              }
                            ]
                          },
                          "task_location": {
                            "list_id": 1560300071,
                            "folder_id": 468300080,
                            "space_id": 22800253,
                            "list_name": "List",
                            "folder_name": "Folder",
                            "space_name": "Space"
                          },
                          "task_tags": [
                            {
                              "name": "content-request",
                              "tag_fg": "#800000",
                              "tag_bg": "#2ecd6f",
                              "creator": 301828
                            },
                            {
                              "name": "marketing-okr",
                              "tag_fg": "#800000",
                              "tag_bg": "#7C4DFF",
                              "creator": 301828
                            }
                          ],
                          "task_url": "https://staging.clickup.com/t/1vwwavv"
                        }
                      ]
                    }
                  ]
                },
                "example": {
                  "data": [
                    {
                      "id": "1963465985517105840",
                      "task": {
                        "id": "1vwwavv",
                        "custom_id": "JOSH-917",
                        "name": "woof",
                        "status": {
                          "status": "open yes",
                          "color": "#d3d3d3",
                          "type": "open",
                          "orderindex": 0
                        },
                        "custom_type": null
                      },
                      "wid": "300702",
                      "user": {
                        "id": 1,
                        "username": "first_name last_name",
                        "email": "test@gmail.com",
                        "color": "#08c7e0",
                        "initials": "JK",
                        "profilePicture": "https://attachments.clickup.com/profilePictures/1_HHk.jpg"
                      },
                      "billable": false,
                      "start": 1592841559129,
                      "end": 1592845899021,
                      "duration": "4339892",
                      "description": "",
                      "tags": [],
                      "source": "clickup",
                      "at": "1592845899021",
                      "task_location": {
                        "list_id": 1560300071,
                        "folder_id": 468300080,
                        "space_id": 22800253,
                        "list_name": "List",
                        "folder_name": "Folder",
                        "space_name": "Space"
                      },
                      "task_tags": [
                        {
                          "name": "content-request",
                          "tag_fg": "#800000",
                          "tag_bg": "#2ecd6f",
                          "creator": 301828
                        },
                        {
                          "name": "marketing-okr",
                          "tag_fg": "#800000",
                          "tag_bg": "#7C4DFF",
                          "creator": 301828
                        }
                      ],
                      "task_url": "https://staging.clickup.com/t/1vwwavv"
                    }
                  ]
                }
              }
            }
          }
        },
        "deprecated": false
      },
      "parameters": []
    }
  },
  "components": {
    "securitySchemes": {
      "Authorization_Token": {
        "name": "Authorization",
        "type": "apiKey",
        "in": "header",
        "description": "API token required for authentication. Two types of tokens are supported:\n**Personal API Key** Obtain from ClickUp's settings page under 'Apps' and add it to the header as `Authorization: pk_...`\n**OAuth2 Access Token** Generated through the OAuth2 flow and add it to the header as `Authorization: Bearer {access_token}`"
      }
    }
  },
  "security": [
    {
      "Authorization_Token": []
    }
  ],
  "tags": [
    {
      "name": "Time Tracking"
    }
  ]
}
```