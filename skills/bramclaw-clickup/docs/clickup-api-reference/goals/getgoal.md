# Get Goal

View the details of a Goal including its Targets.

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
    "/v2/goal/{goal_id}": {
      "get": {
        "summary": "Get Goal",
        "tags": [
          "Goals"
        ],
        "description": "View the details of a Goal including its Targets.",
        "operationId": "GetGoal",
        "parameters": [
          {
            "name": "goal_id",
            "in": "path",
            "description": "900e-462d-a849-4a216b06d930 (uuid)",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "e53a033c"
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
                  "title": "GetGoalresponse",
                  "required": [
                    "goal"
                  ],
                  "type": "object",
                  "properties": {
                    "goal": {
                      "title": "Goal",
                      "required": [
                        "id",
                        "name",
                        "team_id",
                        "date_created",
                        "start_date",
                        "due_date",
                        "description",
                        "private",
                        "archived",
                        "creator",
                        "color",
                        "pretty_id",
                        "multiple_owners",
                        "folder_id",
                        "members",
                        "owners",
                        "key_results",
                        "percent_completed",
                        "history",
                        "pretty_url"
                      ],
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        },
                        "team_id": {
                          "type": "string"
                        },
                        "date_created": {
                          "type": "string"
                        },
                        "start_date": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "due_date": {
                          "type": "string"
                        },
                        "description": {
                          "type": "string"
                        },
                        "private": {
                          "type": "boolean"
                        },
                        "archived": {
                          "type": "boolean"
                        },
                        "creator": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "color": {
                          "type": "string"
                        },
                        "pretty_id": {
                          "type": "string"
                        },
                        "multiple_owners": {
                          "type": "boolean"
                        },
                        "folder_id": {
                          "type": [
                            "string",
                            "null"
                          ]
                        },
                        "members": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          },
                          "description": ""
                        },
                        "owners": {
                          "type": "array",
                          "items": {
                            "title": "Owner",
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
                          "description": ""
                        },
                        "key_results": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          },
                          "description": ""
                        },
                        "percent_completed": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "history": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          },
                          "description": ""
                        },
                        "pretty_url": {
                          "type": "string"
                        }
                      },
                      "examples": [
                        {
                          "id": "e53a033c-900e-462d-a849-4a216b06d930",
                          "name": "Goal Name",
                          "team_id": "512",
                          "date_created": "1568044355026",
                          "start_date": null,
                          "due_date": "1568036964079",
                          "description": "Goal Description",
                          "private": false,
                          "archived": false,
                          "creator": 183,
                          "color": "#32a852",
                          "pretty_id": "6",
                          "multiple_owners": true,
                          "folder_id": null,
                          "members": [],
                          "owners": [
                            {
                              "id": 183,
                              "username": "John Doe",
                              "initials": "JD",
                              "email": "johndoe@gmail.com",
                              "color": "#827718",
                              "profilePicture": "https://attachments-public.clickup.com/profilePictures/183_abc.jpg"
                            }
                          ],
                          "key_results": [],
                          "percent_completed": 0,
                          "history": [],
                          "pretty_url": "https://app.clickup.com/512/goals/6"
                        }
                      ]
                    }
                  },
                  "examples": [
                    {
                      "goal": {
                        "id": "e53a033c-900e-462d-a849-4a216b06d930",
                        "name": "Updated Goal Name",
                        "team_id": "512",
                        "date_created": "1568044355026",
                        "start_date": null,
                        "due_date": "1568036964079",
                        "description": "Updated Goal Description",
                        "private": false,
                        "archived": false,
                        "creator": 183,
                        "color": "#32a852",
                        "pretty_id": "6",
                        "multiple_owners": true,
                        "folder_id": null,
                        "members": [],
                        "owners": [
                          {
                            "id": 182,
                            "username": "Jane Doe",
                            "initials": "JD",
                            "email": "janedoe@gmail.com",
                            "color": "#827718",
                            "profilePicture": "https://attachments-public.clickup.com/profilePictures/182_abc.jpg"
                          }
                        ],
                        "key_results": [],
                        "percent_completed": 0,
                        "history": [],
                        "pretty_url": "https://app.clickup.com/512/goals/6"
                      }
                    }
                  ]
                },
                "example": {
                  "goal": {
                    "id": "e53a033c-900e-462d-a849-4a216b06d930",
                    "name": "Updated Goal Name",
                    "team_id": "512",
                    "date_created": "1568044355026",
                    "start_date": null,
                    "due_date": "1568036964079",
                    "description": "Updated Goal Description",
                    "private": false,
                    "archived": false,
                    "creator": 183,
                    "color": "#32a852",
                    "pretty_id": "6",
                    "multiple_owners": true,
                    "folder_id": null,
                    "members": [],
                    "owners": [
                      {
                        "id": 182,
                        "username": "Jane Doe",
                        "initials": "JD",
                        "email": "janedoe@gmail.com",
                        "color": "#827718",
                        "profilePicture": "https://attachments-public.clickup.com/profilePictures/182_abc.jpg"
                      }
                    ],
                    "key_results": [],
                    "percent_completed": 0,
                    "history": [],
                    "pretty_url": "https://app.clickup.com/512/goals/6"
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
      "name": "Goals"
    }
  ]
}
```