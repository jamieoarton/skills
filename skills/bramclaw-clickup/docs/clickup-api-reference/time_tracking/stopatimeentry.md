# Stop a time Entry

Stop a timer that's currently running for the authenticated user.

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
    "/v2/team/{team_id}/time_entries/stop": {
      "post": {
        "summary": "Stop a time Entry",
        "tags": [
          "Time Tracking"
        ],
        "description": "Stop a timer that's currently running for the authenticated user.",
        "operationId": "StopatimeEntry",
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
                  "title": "StopatimeEntryresponse",
                  "required": [
                    "data"
                  ],
                  "type": "object",
                  "properties": {
                    "data": {
                      "title": "Data3",
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
                        "at"
                      ],
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "task": {
                          "title": "Task6",
                          "required": [
                            "id",
                            "name",
                            "status",
                            "custom_type"
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
                              "id": "task_id",
                              "name": "test task",
                              "status": {
                                "status": "to do",
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
                          "title": "User2",
                          "required": [
                            "id",
                            "username",
                            "initials",
                            "email",
                            "color",
                            "profilePicture"
                          ],
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "integer",
                              "contentEncoding": "int32"
                            },
                            "username": {
                              "type": "string"
                            },
                            "initials": {
                              "type": "string"
                            },
                            "email": {
                              "type": "string"
                            },
                            "color": {
                              "type": "string"
                            },
                            "profilePicture": {
                              "type": "string"
                            }
                          },
                          "examples": [
                            {
                              "id": 183,
                              "username": "John Doe",
                              "initials": "JD",
                              "email": "johndoe@gmail.com",
                              "color": "#827718",
                              "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                            }
                          ]
                        },
                        "billable": {
                          "type": "boolean"
                        },
                        "start": {
                          "type": "string"
                        },
                        "end": {
                          "type": "integer",
                          "contentEncoding": "int64"
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
                        "source": {
                          "type": "string"
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
                          "end": 1595289452790,
                          "duration": 56948,
                          "description": "",
                          "tags": [],
                          "source": "clickup",
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
                        "end": 1595289452790,
                        "duration": 56948,
                        "description": "",
                        "tags": [],
                        "source": "clickup",
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
                    "end": 1595289452790,
                    "duration": 56948,
                    "description": "",
                    "tags": [],
                    "source": "clickup",
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