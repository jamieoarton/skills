# Get running time entry

View a time entry that's currently tracking time for the authenticated user. \
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
    "/v2/team/{team_id}/time_entries/current": {
      "get": {
        "summary": "Get running time entry",
        "tags": [
          "Time Tracking"
        ],
        "description": "View a time entry that's currently tracking time for the authenticated user. \\\n \\\n***Note:** A time entry that has a negative duration means that timer is currently running for that user.*",
        "operationId": "Getrunningtimeentry",
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
            "name": "assignee",
            "in": "query",
            "description": "user id",
            "style": "form",
            "explode": true,
            "schema": {
              "type": "number",
              "contentEncoding": "double"
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
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "title": "Getrunningtimeentryresponse",
                  "required": [
                    "data"
                  ],
                  "type": "object",
                  "properties": {
                    "data": {
                      "title": "Data",
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
                          "title": "Task5",
                          "required": [
                            "id",
                            "name",
                            "status"
                          ],
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "string"
                            },
                            "name": {
                              "type": "string"
                            },
                            "status": {
                              "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D/get/responses/200/content/application~1json/schema/properties/status"
                            }
                          },
                          "examples": [
                            {
                              "id": "task_id",
                              "name": "task_name",
                              "status": {
                                "status": "to do",
                                "color": "#d3d3d3",
                                "type": "open",
                                "orderindex": 0
                              }
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
                          "type": "string"
                        }
                      },
                      "examples": [
                        {
                          "id": "timer_id",
                          "task": {
                            "id": "task_id",
                            "name": "task_name",
                            "status": {
                              "status": "to do",
                              "color": "#d3d3d3",
                              "type": "open",
                              "orderindex": 0
                            }
                          },
                          "wid": "workspace_id",
                          "user": {
                            "id": 300528,
                            "username": "first_name last_name",
                            "email": "test@gmail.com",
                            "color": "#08c7e0",
                            "initials": "JK",
                            "profilePicture": "https://attachments-public.clickup.com/profilePictures/1_HHk.jpg"
                          },
                          "billable": false,
                          "start": "1595293042560",
                          "duration": -25655,
                          "description": "",
                          "tags": [],
                          "at": "1595293042560"
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
                          "name": "task_name",
                          "status": {
                            "status": "to do",
                            "color": "#d3d3d3",
                            "type": "open",
                            "orderindex": 0
                          }
                        },
                        "wid": "workspace_id",
                        "user": {
                          "id": 300528,
                          "username": "first_name last_name",
                          "email": "test@gmail.com",
                          "color": "#08c7e0",
                          "initials": "JK",
                          "profilePicture": "https://attachments-public.clickup.com/profilePictures/1_HHk.jpg"
                        },
                        "billable": false,
                        "start": "1595293042560",
                        "duration": -25655,
                        "description": "",
                        "tags": [],
                        "at": "1595293042560"
                      }
                    }
                  ]
                },
                "example": {
                  "data": {
                    "id": "timer_id",
                    "task": {
                      "id": "task_id",
                      "name": "task_name",
                      "status": {
                        "status": "to do",
                        "color": "#d3d3d3",
                        "type": "open",
                        "orderindex": 0
                      }
                    },
                    "wid": "workspace_id",
                    "user": {
                      "id": 300528,
                      "username": "first_name last_name",
                      "email": "test@gmail.com",
                      "color": "#08c7e0",
                      "initials": "JK",
                      "profilePicture": "https://attachments-public.clickup.com/profilePictures/1_HHk.jpg"
                    },
                    "billable": false,
                    "start": "1595293042560",
                    "duration": -25655,
                    "description": "",
                    "tags": [],
                    "at": "1595293042560"
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