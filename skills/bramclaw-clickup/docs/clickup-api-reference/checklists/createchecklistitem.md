# Create Checklist Item

Add a line item to a task checklist.

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
    "/v2/checklist/{checklist_id}/checklist_item": {
      "post": {
        "summary": "Create Checklist Item",
        "tags": [
          "Task Checklists"
        ],
        "description": "Add a line item to a task checklist.",
        "operationId": "CreateChecklistItem",
        "parameters": [
          {
            "name": "checklist_id",
            "in": "path",
            "description": "b8a8-48d8-a0c6-b4200788a683 (uuid)",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "b955c4dc"
              ]
            }
          }
        ],
        "requestBody": {
          "description": "",
          "content": {
            "application/json": {
              "schema": {
                "title": "CreateChecklistItemrequest",
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string"
                  },
                  "assignee": {
                    "type": "integer",
                    "contentEncoding": "int32"
                  }
                },
                "examples": [
                  {
                    "name": "Checklist Item",
                    "assignee": 183
                  }
                ]
              },
              "example": {
                "name": "Checklist Item",
                "assignee": 183
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
                  "title": "CreateChecklistItemresponse",
                  "required": [
                    "checklist"
                  ],
                  "type": "object",
                  "properties": {
                    "checklist": {
                      "title": "Checklist1",
                      "required": [
                        "id",
                        "task_id",
                        "name",
                        "date_created",
                        "orderindex",
                        "resolved",
                        "unresolved",
                        "items"
                      ],
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "task_id": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        },
                        "date_created": {
                          "type": "string"
                        },
                        "orderindex": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "resolved": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "unresolved": {
                          "type": "integer",
                          "contentEncoding": "int32"
                        },
                        "items": {
                          "type": "array",
                          "items": {
                            "title": "Item",
                            "required": [
                              "id",
                              "name",
                              "orderindex",
                              "assignee",
                              "resolved",
                              "parent",
                              "date_created",
                              "children"
                            ],
                            "type": "object",
                            "properties": {
                              "id": {
                                "type": "string"
                              },
                              "name": {
                                "type": "string"
                              },
                              "orderindex": {
                                "type": "integer",
                                "contentEncoding": "int32"
                              },
                              "assignee": {
                                "$ref": "#/paths/~1v2~1task~1%7Btask_id%7D~1comment/get/responses/200/content/application~1json/schema/properties/comments/items/properties/assignee"
                              },
                              "resolved": {
                                "type": "boolean"
                              },
                              "parent": {
                                "type": [
                                  "string",
                                  "null"
                                ]
                              },
                              "date_created": {
                                "type": "string"
                              },
                              "children": {
                                "type": "array",
                                "items": {
                                  "type": "string"
                                },
                                "description": ""
                              }
                            },
                            "examples": [
                              {
                                "id": "21e08dc8-e491-47f5-9fd8-d1dc4cedcc6f",
                                "name": "Checklist Item",
                                "orderindex": 0,
                                "assignee": {
                                  "id": 183,
                                  "username": "John Doe",
                                  "email": "example@email.com",
                                  "color": "#827718",
                                  "initials": "JD",
                                  "profilePicture": "https://attachments.clickup.com/profilePictures/183_nx1.jpg"
                                },
                                "resolved": false,
                                "parent": null,
                                "date_created": "1567711566859",
                                "children": []
                              }
                            ]
                          },
                          "description": ""
                        }
                      },
                      "examples": [
                        {
                          "id": "b955c4dc-b8a8-48d8-a0c6-b4200788a683",
                          "task_id": "9hv",
                          "name": "Checklist",
                          "date_created": "1567711563204",
                          "orderindex": 0,
                          "resolved": 0,
                          "unresolved": 1,
                          "items": [
                            {
                              "id": "21e08dc8-e491-47f5-9fd8-d1dc4cedcc6f",
                              "name": "Checklist Item",
                              "orderindex": 0,
                              "assignee": {
                                "id": 183,
                                "username": "John Doe",
                                "email": "example@email.com",
                                "color": "#827718",
                                "initials": "JD",
                                "profilePicture": "https://attachments.clickup.com/profilePictures/183_nx1.jpg"
                              },
                              "resolved": false,
                              "parent": null,
                              "date_created": "1567711566859",
                              "children": []
                            }
                          ]
                        }
                      ]
                    }
                  },
                  "examples": [
                    {
                      "checklist": {
                        "id": "b955c4dc-b8a8-48d8-a0c6-b4200788a683",
                        "task_id": "9hv",
                        "name": "Checklist",
                        "date_created": "1567711563204",
                        "orderindex": 0,
                        "resolved": 0,
                        "unresolved": 1,
                        "items": [
                          {
                            "id": "21e08dc8-e491-47f5-9fd8-d1dc4cedcc6f",
                            "name": "Checklist Item",
                            "orderindex": 0,
                            "assignee": {
                              "id": 183,
                              "username": "John Doe",
                              "email": "example@email.com",
                              "color": "#827718",
                              "initials": "JD",
                              "profilePicture": "https://attachments.clickup.com/profilePictures/183_nx1.jpg"
                            },
                            "resolved": false,
                            "parent": null,
                            "date_created": "1567711566859",
                            "children": []
                          }
                        ]
                      }
                    }
                  ]
                },
                "example": {
                  "checklist": {
                    "id": "b955c4dc-b8a8-48d8-a0c6-b4200788a683",
                    "task_id": "9hv",
                    "name": "Checklist",
                    "date_created": "1567711563204",
                    "orderindex": 0,
                    "resolved": 0,
                    "unresolved": 1,
                    "items": [
                      {
                        "id": "21e08dc8-e491-47f5-9fd8-d1dc4cedcc6f",
                        "name": "Checklist Item",
                        "orderindex": 0,
                        "assignee": {
                          "id": 183,
                          "username": "John Doe",
                          "email": "example@email.com",
                          "color": "#827718",
                          "initials": "JD",
                          "profilePicture": "https://attachments.clickup.com/profilePictures/183_nx1.jpg"
                        },
                        "resolved": false,
                        "parent": null,
                        "date_created": "1567711566859",
                        "children": []
                      }
                    ]
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
      "name": "Task Checklists"
    }
  ]
}
```