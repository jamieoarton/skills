# Create a time entry

Create a time entry. \
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
      "post": {
        "summary": "Create a time entry",
        "tags": [
          "Time Tracking"
        ],
        "description": "Create a time entry. \\\n \\\n***Note:** A time entry that has a negative duration means that timer is currently running for that user.*",
        "operationId": "Createatimeentry",
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
          }
        ],
        "requestBody": {
          "description": "Associate a time entry with a task using the `tid` parameter.",
          "content": {
            "application/json": {
              "schema": {
                "title": "Createatimeentryrequest",
                "required": [
                  "start",
                  "duration"
                ],
                "type": "object",
                "properties": {
                  "description": {
                    "type": "string"
                  },
                  "tags": {
                    "description": "Users on the Business Plan and above can include a time tracking label.",
                    "type": "array",
                    "items": {
                      "title": "Tags6",
                      "required": [
                        "name",
                        "tag_fg",
                        "tag_bg"
                      ],
                      "type": "object",
                      "properties": {
                        "name": {
                          "type": "string"
                        },
                        "tag_fg": {
                          "type": "string"
                        },
                        "tag_bg": {
                          "type": "string"
                        }
                      },
                      "examples": [
                        {
                          "name": "Tag name",
                          "tag_fg": "#000000",
                          "tag_bg": "#000000"
                        }
                      ]
                    }
                  },
                  "start": {
                    "type": "integer",
                    "contentEncoding": "int64"
                  },
                  "stop": {
                    "type": "integer",
                    "contentEncoding": "int64",
                    "description": "The `duration` parameter can be used instead of the `stop` parameter. "
                  },
                  "end": {
                    "type": "integer",
                    "contentEncoding": "int64"
                  },
                  "billable": {
                    "type": "boolean"
                  },
                  "duration": {
                    "description": "When there are values for both `start` and `end`, `duration` is ignored. The `stop` parameter can be used instead of the `duration` parameter.",
                    "type": "integer",
                    "contentEncoding": "int32"
                  },
                  "assignee": {
                    "description": "Workspace owners and admins can include any user id. Workspace members can only include their own user id.",
                    "type": "integer",
                    "contentEncoding": "int32"
                  },
                  "tid": {
                    "type": "string"
                  }
                },
                "examples": [
                  {
                    "description": "from api",
                    "tags": [
                      {
                        "name": "name of tag",
                        "tag_bg": "#BF55EC",
                        "tag_fg": "#FFFFFF"
                      }
                    ],
                    "start": 1595282645000,
                    "end": 1595282660000,
                    "billable": true,
                    "duration": 50000,
                    "assignee": 1,
                    "tid": "task_id"
                  }
                ]
              },
              "example": {
                "description": "from api",
                "tags": [
                  {
                    "name": "name of tag",
                    "tag_bg": "#BF55EC",
                    "tag_fg": "#FFFFFF"
                  }
                ],
                "start": 1595282645000,
                "billable": true,
                "duration": 50000,
                "assignee": 1,
                "tid": "task_id"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "Createatimeentryresponse",
                  "required": [
                    "description",
                    "tags",
                    "start",
                    "billable",
                    "duration",
                    "assignee",
                    "tid"
                  ],
                  "type": "object",
                  "properties": {
                    "description": {
                      "type": "string"
                    },
                    "tags": {
                      "type": "array",
                      "items": {
                        "$ref": "#/paths/~1v2~1team~1%7Bteam_Id%7D~1time_entries/post/requestBody/content/application~1json/schema/properties/tags/items"
                      },
                      "description": ""
                    },
                    "start": {
                      "type": "integer",
                      "contentEncoding": "int64"
                    },
                    "billable": {
                      "type": "boolean"
                    },
                    "duration": {
                      "type": "integer",
                      "contentEncoding": "int32"
                    },
                    "assignee": {
                      "type": "integer",
                      "contentEncoding": "int32"
                    },
                    "tid": {
                      "type": "string"
                    }
                  },
                  "examples": [
                    {
                      "description": "from api",
                      "tags": [
                        {
                          "name": "name of tag",
                          "tag_bg": "#BF55EC",
                          "tag_fg": "#BF55EC"
                        }
                      ],
                      "start": 1595282645000,
                      "billable": true,
                      "duration": 50000,
                      "assignee": 1,
                      "tid": "task_id"
                    }
                  ]
                },
                "example": {
                  "description": "from api",
                  "tags": [
                    {
                      "name": "name of tag",
                      "tag_bg": "#BF55EC",
                      "tag_fg": "#BF55EC"
                    }
                  ],
                  "start": 1595282645000,
                  "billable": true,
                  "duration": 50000,
                  "assignee": 1,
                  "tid": "task_id"
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