# Update a time Entry

Update the details of a time entry.

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
    "/v2/team/{team_id}/time_entries/{timer_id}": {
      "put": {
        "summary": "Update a time Entry",
        "tags": [
          "Time Tracking"
        ],
        "description": "Update the details of a time entry.",
        "operationId": "UpdateatimeEntry",
        "parameters": [
          {
            "name": "team_id",
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
            "name": "timer_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "number",
              "contentEncoding": "double",
              "examples": [
                2004673344540003600
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
            "description": "When the `custom_task_ids` parameter is set to `true`, the Workspace ID must be provided using the `team_id` parameter.\n \\\nFor example: `custom_task_ids=true&team_id=123`",
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
          "description": "Accessible tag actions are `[\"replace\", \"add\", \"remove\"]`",
          "content": {
            "application/json": {
              "schema": {
                "title": "UpdateatimeEntryrequest",
                "required": [
                  "tags",
                  "tid"
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
                      "$ref": "#/paths/~1v2~1team~1%7Bteam_Id%7D~1time_entries/post/requestBody/content/application~1json/schema/properties/tags/items"
                    }
                  },
                  "tag_action": {
                    "type": "string"
                  },
                  "start": {
                    "type": "integer",
                    "contentEncoding": "int64",
                    "description": "When providing `start`, you must also provide `end`."
                  },
                  "end": {
                    "type": "integer",
                    "contentEncoding": "int64",
                    "description": "When providing `end`, you must also provide `start`."
                  },
                  "tid": {
                    "type": "string"
                  },
                  "billable": {
                    "type": "boolean"
                  },
                  "duration": {
                    "type": "integer",
                    "contentEncoding": "int32"
                  }
                },
                "examples": [
                  {
                    "description": "",
                    "tags": [
                      {
                        "name": "name of tag",
                        "tag_bg": "#BF55EC",
                        "tag_fg": "#FFFFFF"
                      }
                    ],
                    "tag_action": "add",
                    "start": 1595289395842,
                    "end": 1595289495842,
                    "tid": "task_id",
                    "billable": true,
                    "duration": 100000
                  }
                ]
              },
              "example": {
                "description": "",
                "tags": [
                  {
                    "name": "name of tag",
                    "tag_bg": "#BF55EC",
                    "tag_fg": "#FFFFFF"
                  }
                ],
                "tag_action": "add",
                "start": 1595289395842,
                "end": 1595289495842,
                "tid": "task_id",
                "billable": true,
                "duration": 100000
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
                  "type": "object",
                  "contentMediaType": "application/json"
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