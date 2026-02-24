# Start a time Entry

Start a timer for the authenticated user.

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
    "/v2/team/{team_Id}/time_entries/start": {
      "post": {
        "summary": "Start a time Entry",
        "tags": [
          "Time Tracking"
        ],
        "description": "Start a timer for the authenticated user.",
        "operationId": "StartatimeEntry",
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
          "description": "For Workspaces on the Free Forever or Unlimited Plan, either the `timer_id` parameter or the `\"tid\"` field in the body of the request are required fields.",
          "content": {
            "application/json": {
              "schema": {
                "title": "StartatimeEntryrequest",
                "type": "object",
                "properties": {
                  "description": {
                    "type": "string"
                  },
                  "tags": {
                    "description": "Users on the Business Plan and above can include a time tracking label.",
                    "type": "array",
                    "items": {
                      "title": "Tags10",
                      "required": [
                        "name"
                      ],
                      "type": "object",
                      "properties": {
                        "name": {
                          "type": "string"
                        }
                      },
                      "examples": [
                        {
                          "name": "name of tag"
                        }
                      ]
                    }
                  },
                  "tid": {
                    "type": "string"
                  },
                  "billable": {
                    "type": "boolean"
                  }
                },
                "examples": [
                  {
                    "description": "from api",
                    "tags": [
                      {
                        "name": "tag1"
                      }
                    ],
                    "tid": "task_id",
                    "billable": false
                  }
                ]
              },
              "example": {
                "description": "from api",
                "tags": [
                  {
                    "name": "tag1"
                  }
                ],
                "tid": "task_id",
                "billable": false
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
                  "title": "StartatimeEntryresponse",
                  "required": [
                    "data"
                  ],
                  "type": "object",
                  "properties": {
                    "data": {
                      "title": "Data2",
                      "required": [
                        "id",
                        "task",
                        "wid",
                        "user",
                        "billable",
                        "start",
                        "duration",
                        "description",
                        "tags",
                        "at"
                      ],
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "task": {
                          "$ref": "#/paths/~1v2~1team~1%7Bteam_id%7D~1time_entries~1stop/post/responses/200/content/application~1json/schema/properties/data/properties/task"
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
                        "duration": {
                          "type": "integer",
                          "contentEncoding": "int32"
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
                        "at": {
                          "type": "integer",
                          "contentEncoding": "int64"
                        }
                      },
                      "examples": [
                        {
                          "id": "timer_id",
                          "task": {
                            "id": "task_id",
                            "name": "test task",
                            "status": {
                              "status": "to do",
                              "color": "#d3d3d3",
                              "type": "open",
                              "orderindex": 0
                            },
                            "custom_type": null
                          },
                          "wid": "workspace_id",
                          "user": {
                            "id": 1,
                            "username": "first_name last_name",
                            "email": "test@gmail.com",
                            "color": "#08c7e0",
                            "initials": "JK",
                            "profilePicture": "https://attachments-public.clickup.com/profilePictures/1_HHk.jpg"
                          },
                          "billable": false,
                          "start": "1595289395842",
                          "duration": -53,
                          "description": "",
                          "tags": [],
                          "at": 1595289452790
                        }
                      ]
                    }
                  },
                  "examples": [
                    {
                      "data": {
                        "id": "timer_id",
                        "task": {
                          "id": "task_id",
                          "name": "test task",
                          "status": {
                            "status": "to do",
                            "color": "#d3d3d3",
                            "type": "open",
                            "orderindex": 0
                          },
                          "custom_type": null
                        },
                        "wid": "workspace_id",
                        "user": {
                          "id": 1,
                          "username": "first_name last_name",
                          "email": "test@gmail.com",
                          "color": "#08c7e0",
                          "initials": "JK",
                          "profilePicture": "https://attachments-public.clickup.com/profilePictures/1_HHk.jpg"
                        },
                        "billable": false,
                        "start": "1595289395842",
                        "duration": -53,
                        "description": "",
                        "tags": [],
                        "at": 1595289452790
                      }
                    }
                  ]
                },
                "example": {
                  "data": {
                    "id": "timer_id",
                    "task": {
                      "id": "task_id",
                      "name": "test task",
                      "status": {
                        "status": "to do",
                        "color": "#d3d3d3",
                        "type": "open",
                        "orderindex": 0
                      },
                      "custom_type": null
                    },
                    "wid": "workspace_id",
                    "user": {
                      "id": 1,
                      "username": "first_name last_name",
                      "email": "test@gmail.com",
                      "color": "#08c7e0",
                      "initials": "JK",
                      "profilePicture": "https://attachments-public.clickup.com/profilePictures/1_HHk.jpg"
                    },
                    "billable": false,
                    "start": "1595289395842",
                    "duration": -53,
                    "description": "",
                    "tags": [],
                    "at": 1595289452790
                  }
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